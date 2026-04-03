from django.shortcuts import render
from .models import Product, Collection


def product_list(request):
    products = (
        Product.objects
        .filter(is_active=True, collection__city__is_active=True)
        .select_related('collection', 'collection__city')
        .prefetch_related('images')
    )

    featured_collection = (
        Collection.objects
        .filter(
            is_featured=True,
            release_status='available',
            city__is_active=True,
        )
        .select_related('city')
        .first()
    )

    coming_soon_collections = (
        Collection.objects
        .filter(
            release_status='coming_soon',
            city__is_active=True,
        )
        .select_related('city')[:2]
    )

    context = {
        'products': products,
        'featured_collection': featured_collection,
        'coming_soon_collections': coming_soon_collections,
    }

    return render(request, 'products/product_list.html', context)
