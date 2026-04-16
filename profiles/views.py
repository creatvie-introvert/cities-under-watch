from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404

from checkout.models import Order
from products.models import ProductDownload


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


@login_required
def profile_downloads(request):
    """Display all downloadable files purchased by the user."""
    profile = request.user.userprofile

    downloads = ProductDownload.objects.filter(
        product__orderlineitem__order__user=request.user
    ).distinct().order_by('product__title', 'sort_order')

    context = {
        'profile': profile,
        'downloads': downloads,
        'on_profile_page': True,
    }

    return render(request, 'profiles/profile_downloads.html', context)


@login_required
def account_download_file(request, download_id):
    """Serve a purchased download file to the logged-in user."""
    download = get_object_or_404(ProductDownload, pk=download_id)

    has_access = Order.objects.filter(
        user=request.user,
        lineitems__product=download.product,
    ).exists()

    if not has_access:
        raise Http404("You do not have access to this file.")

    if not download.file:
        raise Http404("File not found.")

    return FileResponse(
        download.file.open('rb'),
        as_attachment=True,
        filename=download.file.name.split('/')[-1],
    )
