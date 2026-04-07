from django.contrib import admin
from .models import City, Collection, CollectionNarrativePanel, Product, ProductImage


class CollectionNarrativePanelInline(admin.TabularInline):
    model = CollectionNarrativePanel
    extra = 4
    fields = (
        'panel_number',
        'title',
        'text',
        'label',
        'image',
        'image_alt',
    )
    ordering = ('panel_number',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city',
        'release_status',
        'is_featured',
        'created_at',
        'updated_at',
    )
    list_filter = ('release_status', 'is_featured', 'city',)
    search_fields = ('name', 'slug', 'city_name')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CollectionNarrativePanelInline]


@admin.register(CollectionNarrativePanel)
class CollectionNarrativePanelAdmin(admin.ModelAdmin):
    list_display = ('collection', 'panel_number', 'title', 'label')
    list_filter = ('collection',)
    search_fields = ('collection__name', 'title', 'label')
    ordering = ('collection', 'panel_number')


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'collection',
        'sku',
        'price',
        'is_active',
        'is_featured',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'is_featured',
        'collection__city',
        'collection',
    )
    search_fields = (
        'title',
        'slug',
        'sku',
        'collection__name',
        'collection_city_name',
    )
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_primary', 'sort_order', 'created_at')
    list_filter = ('is_primary',)
    search_fields = ('product__title', 'alt_text')
