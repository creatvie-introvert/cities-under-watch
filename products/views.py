from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404

from .models import Product, Collection
from core.forms import NewsletterSubscriberForm


def product_list(request):
    query = request.GET.get('q', '').strip()
    selected_collection = request.GET.get('collection', '').strip()
    products_limit = 9
    page = request.GET.get('page', '1').strip()

    try:
        page = int(page)
    except ValueError:
        page = 1

    if page < 1:
        page = 1

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

    total_products = products.count()
    products_to_show = page * products_limit
    has_more_products = total_products > products_to_show
    next_page = page + 1 if has_more_products else None
    products = products[:products_to_show]

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

    newsletter_form = NewsletterSubscriberForm()

    context = {
        'products': products,
        'featured_collection': featured_collection,
        'coming_soon_collections': coming_soon_collections,
        'search_term': query,
        'available_collections': available_collections,
        'selected_collection': selected_collection,
        'has_more_products': has_more_products,
        'next_page': next_page,
        'newsletter_form': newsletter_form,
    }

    return render(request, 'products/product_list.html', context)


def collection_list(request):
    collections = (
        Collection.objects
        .filter(
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
        .order_by('name')
    )

    newsletter_form = NewsletterSubscriberForm()

    context = {
        'collections': collections,
        'newsletter_form': newsletter_form,
    }

    return render(request, 'products/collection_list.html', context)


def collection_detail(request, slug):
    collection = get_object_or_404(
        Collection.objects
        .filter(
            release_status=Collection.ReleaseStatus.AVAILABLE,
            city__is_active=True,
        )
        .select_related('city')
        .annotate(
            product_count=Count(
                'products',
                filter=Q(products__is_active=True)
            )
        ),
        slug=slug,
    )

    collection_products = (
        Product.objects
        .filter(
            is_active=True,
            collection=collection,
            collection__city__is_active=True,
        )
        .select_related('collection', 'collection__city')
        .prefetch_related('images')
        .order_by('title')
    )

    other_collections = (
        Collection.objects
        .filter(
            release_status=Collection.ReleaseStatus.AVAILABLE,
            city__is_active=True,
        )
        .exclude(id=collection.id)
        .select_related('city')
        .annotate(
            product_count=Count(
                'products',
                filter=Q(products__is_active=True)
            )
        )
        .order_by('name')[:3]
    )

    context = {
        'collection': collection,
        'collection_products': collection_products,
        'other_collections': other_collections,
    }

    return render(request, 'products/collection_detail.html', context)


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects
        .filter(
            is_active=True,
            collection__city__is_active=True,
        )
        .select_related('collection', 'collection__city')
        .prefetch_related('images'),
        slug=slug,
    )

    related_products = (
        Product.objects
        .filter(
            is_active=True,
            collection=product.collection,
            collection__city__is_active=True,
        )
        .exclude(id=product.id)
        .select_related('collection', 'collection__city')
        .prefetch_related('images')[:4]
    )

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'products/product_detail.html', context)
