from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'created_at',
        'updated_at',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )

    fields = (
        'order_number',
        'user',
        'full_name',
        'email',
        'phone_number',
        'country_code',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'created_at',
        'updated_at',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )

    list_display = (
        'order_number',
        'user',
        'full_name',
        'email',
        'phone_number',
        'town_or_city',
        'created_at',
        'order_total',
        'grand_total',
    )

    ordering = ('-created_at',)
