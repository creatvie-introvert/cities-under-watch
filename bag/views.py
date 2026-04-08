from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


def view_bag(request):
    """Render the shopping bag page."""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a product to the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if str(item_id) in bag:
        messages.info(request, f'"{product.title}" is already in your bag.')
    else:
        bag[str(item_id)] = 1
        messages.success(request, f'Added "{product.title}" to your bag.' )
    
    request.session['bag'] = bag

    return redirect(redirect_url)
