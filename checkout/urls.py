from django.urls import path

from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'success/<order_number>/',
        views.checkout_success,
        name='checkout_success',
    ),
    path(
        'cache-checkout-data/',
        views.cache_checkout_data,
        name='cache_checkout_data',
    ),
    path(
        'success/<order_number>/download/<int:download_id>/',
        views.download_order_file,
        name='download_order_file',
    ),
    path('wh/', views.stripe_webhook, name='stripe_webhook'),
]
