from django.db.models import Count, Q
from django.shortcuts import render
from .models import Product, Collection


def product_list(request):
    query = request.GET.get('q', '').strip()
    selected_collection = request.GET.get('collection', '').strip()

    products = (
        Product.objects
        .filter(is_active=True, collection__city__is_active=True)
        .select_related('collection', 'collection__city')
        .prefetch_related('images')
    )

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(collection__name__icontains=query)
        ).distinct()

    if selected_collection:
        products = products.filter(collection__slug=selected_collection)

    featured_collection = (
        Collection.objects
        .filter(
            is_featured=True,
            release_status=Collection.ReleaseStatus.AVAILABLE,
            city__is_active=True,
        )
        .select_related('city')
        .annotate(
            product_count=Count(
                'products',
                filter=Q(products__is_active=True)
            )
        )
        .first()
    )

    coming_soon_collections = (
        Collection.objects
        .filter(
            release_status=Collection.ReleaseStatus.COMING_SOON,
            city__is_active=True,
        )
        .select_related('city')[:2]
    )

    for collection in coming_soon_collections:
        collection.product_count = collection.planned_product_count

    available_collections = (
        Collection.objects
        .filter(
            release_status=Collection.ReleaseStatus.AVAILABLE,
            city__is_active=True,
        )
        .select_related('city')
        .order_by('name')
    )

    context = {
        'products': products,
        'featured_collection': featured_collection,
        'coming_soon_collections': coming_soon_collections,
        'search_term': query,
        'available_collections': available_collections,
        'selected_collection': selected_collection,
    }

    return render(request, 'products/product_list.html', context)
