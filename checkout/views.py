import json

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from bag.contexts import bag_contents
from products.models import Product, ProductDownload
from .forms import OrderForm
from .models import Order, OrderLineItem
from profiles.forms import UserProfileForm

User = get_user_model()


def _get_user_from_metadata(user_id):
    """Return a user from Stripe metadata, or None for guest checkout."""
    if not user_id or user_id == 'anonymous':
        return None

    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return None


def _update_profile_from_order(user, order):
    """Update a user's profile from order billing details."""
    profile = user.userprofile

    profile_data = {
        'full_name': order.full_name,
        'phone_number': order.phone_number,
        'country_code': order.country_code,
        'postcode': order.postcode,
        'town_or_city': order.town_or_city,
        'street_address1': order.street_address1,
        'street_address2': order.street_address2,
        'county': order.county,
    }

    profile_form = UserProfileForm(profile_data, instance=profile)
    if profile_form.is_valid():
        profile_form.save()


def _send_order_confirmation_email(request, order):
    """Send a plain-text order confirmation email."""
    subject = f'Cities Under Watch order confirmation - {order.order_number}'

    message = render_to_string(
        'checkout/emails/order_confirmation_email.txt',
        {
            'order': order,
            'request': request,
        },
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.ORDER_CONFIRMATION_FROM_EMAIL,
        recipient_list=[order.email],
        fail_silently=False,
    )


@csrf_exempt
def cache_checkout_data(request):
    """Store checkout metadata on the PaymentIntent before confirmation."""
    if request.method != 'POST':
        return HttpResponse(status=405)

    try:
        client_secret = request.POST.get('client_secret', '')
        stripe_pid = client_secret.split('_secret')[0]

        save_info = 'true' if request.POST.get('save_info') == 'on' else 'false'
        bag = request.session.get('bag', {})

        user_id = request.user.id if request.user.is_authenticated else 'anonymous'

        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            stripe_pid,
            metadata={
                'bag': json.dumps(bag),
                'save_info': save_info,
                'user_id': str(user_id),
            },
        )

        return HttpResponse(status=200)

    except Exception as error:
        messages.error(
            request,
            'Sorry, your payment cannot be processed right now. Please try again later.',
        )
        return HttpResponse(content=str(error), status=400)


def checkout(request):
    """Render the checkout page display and order creation."""
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, 'There is nothing in your basket.')
        return redirect(reverse("product_list"))

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'country_code': request.POST.get('country_code'),
            'postcode': request.POST.get('postcode'),
            'town_or_city': request.POST.get('town_or_city'),
            'street_address1': request.POST.get('street_address1'),
            'street_address2': request.POST.get('street_address2'),
            'county': request.POST.get('county'),
        }

        order_form = OrderForm(form_data)
        save_info = request.POST.get('save_info')

        if order_form.is_valid():
            client_secret = request.POST.get('client_secret', '')
            stripe_pid = client_secret.split('_secret')[0]

            if not stripe_pid:
                messages.error(
                    request,
                    'There was a problem identifying your payment. Please try again.'
                )
                return redirect(reverse('checkout'))

            order = order_form.save(commit=False)
            order.original_bag = json.dumps(bag)
            order.stripe_pid = stripe_pid

            if request.user.is_authenticated:
                order.user = request.user

            order.save()

            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(pk=item_id)

                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products in your basket wasn't found "
                            "in our database. "
                            "Please contact us for assistance."
                        ),
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = save_info
            return redirect(
                reverse('checkout_success', args=[order.order_number])
            )

        messages.error(
            request,
            'There was an error with your form. Please check your details.',
        )
    else:
        current_bag = bag_contents(request)
        total = current_bag['total']

        if not settings.STRIPE_SECRET_KEY:
            messages.error(
                request,
                'Payment configuration is missing. Please try again later.',
            )
            return redirect(reverse('view_bag'))

        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            intent = stripe.PaymentIntent.create(
                amount=round(total * 100),
                currency=settings.STRIPE_CURRENCY,
                metadata={
                    'bag': json.dumps(bag),
                    'save_info': 'false',
                    'user_id': str(request.user.id) if request.user.is_authenticated else 'anonymous',
                }
            )

        except stripe.error.StripeError:
            print(f'Stripe PaymentIntent error: {error}')
            messages.error(
                request,
                'There was a problem connectin to payment services. Please try again.',
            )
            return redirect(reverse('view_bag'))

        if not settings.STRIPE_PUBLIC_KEY:
            messages.warning(
                request,
                'Stripe public key is missing. ',
                'Did you forget to set it in your environment?',
            )

        if request.user.is_authenticated:
            profile = request.user.userprofile

            initial_data = {
                'email': request.user.email,
            }

            if profile:
                initial_data.update({
                    'full_name': profile.full_name,
                    'phone_number': profile.phone_number,
                    'country_code': profile.country_code,
                    'postcode': profile.postcode,
                    'town_or_city': profile.town_or_city,
                    'street_address1': profile.street_address1,
                    'street_address2': profile.street_address2,
                    'county': profile.county,
                })
            
            order_form = OrderForm(initial=initial_data)
        else:
            order_form = OrderForm()

        context = {
            'order_form': order_form,
            'bag_items': current_bag['bag_items'],
            'total': current_bag['total'],
            'product_count': current_bag['product_count'],
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret,
        }

        return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """Handle successful checkouts."""
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        save_info = request.session.get('save_info')

        order.user = request.user
        order.save()

        if save_info:
            profile = request.user.userprofile
            profile_data = {
                'full_name': order.full_name,
                'phone_number': order.phone_number,
                'country_code': order.country_code,
                'postcode': order.postcode,
                'town_or_city': order.town_or_city,
                'street_address1': order.street_address1,
                'street_address2': order.street_address2,
                'county': order.county,
            }

            profile_form = UserProfileForm(profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save()

    _send_order_confirmation_email(request, order)

    messages.success(
        request,
        f'Order successfully processed. Your order number is {order_number}.',
    )

    if 'bag' in request.session:
        del request.session['bag']

    if 'save_info' in request.session:
        del request.session['save_info']

    context = {
        'order': order,
    }

    return render(
        request,
        'checkout/checkout_success.html',
        context,
    )


def download_order_file(request, order_number, download_id):
    """Serve a download file only if it belongs to a purchased product."""
    order = get_object_or_404(Order, order_number=order_number)
    download = get_object_or_404(ProductDownload, pk=download_id)

    purchased_product_ids = order.lineitems.values_list(
        'product_id',
        flat=True,
    )

    if download.product_id not in purchased_product_ids:
        raise Http404("This file is not available for this order.")

    if not download.file:
        raise Http404('File not found.')

    return FileResponse(
        download.file.open('rb'),
        as_attachment=True,
        filename=download.file.name.split('/')[-1],
    )


@csrf_exempt
def stripe_webhook(request):
    """Handle Stripe webhooks."""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    if not settings.STRIPE_WH_SECRET:
        return HttpResponse(status=500)

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WH_SECRET,
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        stripe_pid = intent['id']
        metadata = intent['metadata']
        
        user = _get_user_from_metadata(metadata.get('user_id'))
        save_info = metadata.get('save_info') == 'true'

        try:
            order = Order.objects.get(stripe_pid=stripe_pid)
            print(
                f"Webhook matched order {order.order_number} "
                f"to PaymentIntent {stripe_pid}"
            )

            if user and order.user is None:
                order.user = user
                order.save()

            if user and save_info:
                _update_profile_from_order(user, order)
            
        except Order.DoesNotExist:
            print(
                f"Webhook could not find an order for PaymentIntent "
                f"{stripe_pid}. Attempting recovery"
            )

            try:
                bag_json = metadata.get('bag', '')
                bag = json.loads(bag_json) if bag_json else {}

                if not bag:
                    print(
                        f"Webhook recovery failed for PaymentIntent "
                        f"{stripe_pid}: bag metadata missing"
                    )
                    return HttpResponse(status=200)

                charges = intent['charges']['data']
                billing_details = {}
                address = {}

                if charges:
                    billing_details = charges[0]['billing_details']
                    if billing_details.get('address'):
                        address = billing_details['address']

                recovered_order = Order.objects.create(
                    user=user,
                    full_name=billing_details.get('name', 'Unknown'),
                    email=billing_details.get('email', ''),
                    phone_number=billing_details.get('phone', ''),
                    country_code=address.get('country', '') or 'GB',
                    postcode=address.get('postal_code', ''),
                    town_or_city=address.get('city', ''),
                    street_address1=address.get('line1', ''),
                    street_address2=address.get('line2', ''),
                    county=address.get('state', ''),
                    original_bag=json.dumps(bag),
                    stripe_pid=stripe_pid,
                )

                for item_id, quantity in bag.items():
                    product = Product.objects.get(pk=item_id)
                    OrderLineItem.objects.create(
                        order=recovered_order,
                        product=product,
                        quantity=quantity,
                    )
                
                if user and save_info:
                    _update_profile_from_order(user, recovered_order)

                print(
                    f"Webhook recovered missing order "
                    f"{recovered_order.order_number} for PaymentIntent {stripe_pid}"
                )

            except Product.DoesNotExist:
                print(
                    f"Webhook recovery failed for paymentIntent {stripe_pid}: "
                    f"product missing."
                )

            except Exception as error:
                print(
                    f"Webhook recovery failed for paymentIntent {stripe_pid}: "
                    f"{error}"
                )

    elif event['type'] == 'payment_intent.payment_failed':
        intent = event['data']['object']
        print(f"PaymentIntent failed: {intent['id']}")

    return HttpResponse(status=200)
