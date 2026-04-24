from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import ProductForm, ProductImageForm
from .models import Product, Collection, ProductImage
from core.forms import NewsletterSubscriberForm


def _require_superuser(request):
    """Redirect non-superusers away from product admin views."""
    if not request.user.is_authenticated or not request.user.is_superuser:
        messages.error(
            request,
            'Only store owners can access product management.',
        )
        return redirect(reverse('home'))
    return None


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

    newsletter_form = NewsletterSubscriberForm()

    context = {
        'collection': collection,
        'collection_products': collection_products,
        'other_collections': other_collections,
        'newsletter_form': newsletter_form,
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
        .prefetch_related('images')[:3]
    )

    newsletter_form = NewsletterSubscriberForm()

    context = {
        'product': product,
        'related_products': related_products,
        'newsletter_form': newsletter_form,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """Allow superusers to add a product."""
    access_denied = _require_superuser(request)
    if access_denied:
        return access_denied

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save()
            messages.success(
                request,
                f'Product "{product.title}" was added successfully.',
            )
            return redirect('product_detail', slug=product.slug)

        messages.error(
            request,
            'There was a problem adding the product. Please check the form.',
        )
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


def edit_product(request, slug):
    """Allow superusers to edit an existing product."""
    access_denied = _require_superuser(request)
    if access_denied:
        return access_denied
    
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            product = form.save()
            messages.success(
                request,
                f'Product "{product.title}" was updated successfully.',
            )
            return redirect('product_detail', slug=product.slug)
        
        messages.error(
            request,
            'There was a problem updating the product. Please check the form.',
        )
    else:
        form = ProductForm(instance=product)
        messages.info(
            request,
            f'You are editing "{product.title}".',
        )
    
    context = {
        'form': form,
        'product': product,
        'image_form': ProductImageForm(),
        'product_images': product.images.all(),
    }

    return render(request, 'products/edit_product.html', context)


def delete_product(request, slug):
    """Allow superusers to delete an existing product."""
    access_denied = _require_superuser(request)
    if access_denied:
        return access_denied
    
    product = get_object_or_404(Product, slug=slug)
    product_title = product.title

    if request.method == 'POST':
        product.delete()
        messages.success(
            request,
            f'Product "{product_title}" was deleted successfully.',
        )
        return redirect('product_list')
    
    context = {
        'product': product,
    }

    return render(request, 'products/delete_product.html', context)


def add_product_image(request, slug):
    """Allow superusers to add an image to a product."""
    access_denied = _require_superuser(request)
    if access_denied:
        return access_denied
    
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)

        if form.is_valid():
            product_image = form.save(commit=False)
            product_image.product = product

            if product_image.is_primary:
                ProductImage.objects.filter(product=product).update(is_primary=False)
            
            product_image.save()
            messages.success(
                request,
                f'Image added to "{product.title}" successfully.',
            )
        else:
            messages.error(
                request,
                'There was a problem adding the image. Please check the form.',
            )

    return redirect('edit_product', slug=product.slug)


def edit_product_image(request, slug, image_id):
    """Allow superusers to edit an existing product image."""
    access_denied = _require_superuser(request)
    if access_denied:
        return access_denied
    
    product = get_object_or_404(Product, slug=slug)
    product_image = get_object_or_404(ProductImage, pk=image_id, product=product)

    if request.method == 'POST':
        post_data = request.POST.copy()

        if 'is_primary' not in post_data:
            post_data['is_primary'] = ''
        
        form = ProductImageForm(post_data, request.FILES, instance=product_image)

        if form.is_valid():
            updated_image = form.save(commit=False)

            if updated_image.is_primary:
                ProductImage.objects.filter(product=product).exclude(pk=updated_image.pk).update(is_primary=False)

            updated_image.save()
            messages.success(
                request,
                f'Image for "{product.title}" updated successfully.',
            )
        else:
            messages.error(
                request,
                'There was a problem updating the image. Please check the form.',
            )
    
    return redirect('edit_product', slug=product.slug)


def delete_product_image(request, slug, image_id):
    """Allow superusers to delete a product image."""
    access_denied = _require_superuser(request)
    if access_denied:
        return access_denied
    
    product = get_object_or_404(Product, slug=slug)
    product_image = get_object_or_404(ProductImage, pk=image_id, product=product)

    if request.method == 'POST':
        product_image.delete()
        messages.success(
            request,
            f'Image removed from "{product.title}" successfully.',
        )
    
    return redirect('edit_product', slug=product.slug)