from django.shortcuts import render
from .models import Product


def product_list(request):
    products = (
        Product.objects
        .filter(is_active=True, collection__city__is_active=True)
        .select_related('collection', 'collection__city')
        .prefetch_related('images')
    )

    context = {
        'products': products,
    }

    return render(request, 'products/product_list.html', context)
