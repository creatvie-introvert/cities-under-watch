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
