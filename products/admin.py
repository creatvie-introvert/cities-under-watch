from django.contrib import admin
from .models import City, Collection, Product, ProductImage


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
