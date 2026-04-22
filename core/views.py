from django.shortcuts import render
from products.models import Product


def index(request):
    """Render the home page."""
    featured_products = (
        Product.objects
        .filter(
            is_active=True,
            is_featured=True,
            collection__city__is_active=True,
        )
        .select_related('collection', 'collection__city')
        .prefetch_related('images')[:3]
    )

    context = {
        'featured_products': featured_products,
    }

    return render(request, 'core/index.html', context)


def about(request):
    """Render the about page."""
    return render(request, 'core/about.html')


def contact(request):
    """Render the contact page."""
    return render(request, 'core/contact.html')


def faq(request):
    """Render the FAQ page."""
    return render(request, 'core/faq.html')


def privacy_policy(request):
    """Render the privacy policy page."""
    return render(request, 'core/privacy_policy.html')


def terms_and_conditions(request):
    """Render the terms and conditions page."""
    return render(request, 'core/terms_and_conditions.html')


def refund_policy(request):
    """Render the refund policy page."""
    return render(request, 'core/refund_policy.html')


def delivery_policy(request):
    """Render the delivery policy page."""
    return render(request, 'core/delivery_policy.html')
