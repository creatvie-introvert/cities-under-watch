from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from checkout.models import Order
from .forms import UserProfileForm


@login_required
def profile(request):
    """Display and update the user's profile."""
    profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
    else:
        form = UserProfileForm(instance=profile)

    recent_orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')[:3]

    context = {
        'form': form,
        'recent_orders': recent_orders,
        'on_profile_page': True,
    }

    return render(request, 'profiles/profile.html', context)
