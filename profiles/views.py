from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from checkout.models import Order


@login_required
def profile(request):
    """Display the user's account dashboard."""
    profile = request.user.userprofile

    recent_orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')[:3]

    context = {
        'profile': profile,
        'recent_orders': recent_orders,
        'on_profile_page': True,
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def profile_orders(request):
    """Display the user's full order history."""
    profile = request.user.userprofile

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    context = {
        'profile': profile,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, 'profiles/profile_orders.html', context)
