from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
import stripe

from bag.contexts import bag_contents
from .forms import OrderForm


def checkout(request):
    """Render the checkout page."""
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, 'There is nothing in your basket')
        return redirect(reverse("product_list"))

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
            'Stripe public key is missing. Did you forget ',
            'to set it in your environment?',
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
