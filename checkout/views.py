import json

import stripe
from django.conf import settings
from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse

from bag.contexts import bag_contents
from products.models import Product, ProductDownload
from .forms import OrderForm
from .models import Order, OrderLineItem


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

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.original_bag = json.dumps(bag)
            order.stripe_pid = request.POST.get(
                'client_secret', ''
            ).split('_secret')[0]
            order.save()

            for item_id, qunatity in bag.items():
                try:
                    product = Product.objects.get(pk=item_id)

                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=qunatity,
                    )
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products in your baskest wasn't found "
                            "in our database. "
                            "Please contact us for assistance."
                        ),
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

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

        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=round(total * 100),
            currency=settings.STRIPE_CURRENCY,
        )

        if not settings.STRIPE_PUBLIC_KEY:
            messages.warning(
                request,
                'Stripe public key is missing. ',
                'Did you forget to set it in your environment?',
            )

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

    messages.success(
        request,
        f'Order successfully processed. Your order number is {order_number}.',
    )

    if 'bag' in request.session:
        del request.session['bag']

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
