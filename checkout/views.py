from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from bag.contexts import bag_contents
from .forms import OrderForm


def checkout(request):
    """Render the checkout page."""
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, 'There is nothing in your basket')
        return redirect(reverse("product_list"))

    order_form = OrderForm()
    current_bag = bag_contents(request)

    context = {
        'order_form': order_form,
        'bag_items': current_bag['bag_items'],
        'total': current_bag['total'],
        'product_count': current_bag['product_count'],
    }

    return render(request, 'checkout/checkout.html', context)
