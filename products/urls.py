from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<slug:slug>/', views.edit_product, name='edit_product'),
    path('delete/<slug:slug>/', views.delete_product, name='delete_product'),
    path(
        'edit/<slug:slug>/images/add/',
        views.add_product_image,
        name='add_product_image',
    ),
    path(
        'edit/<slug:slug>/images/<int:image_id>/edit/',
        views.edit_product_image,
        name='edit_product_image',
    ),
    path(
        'edit/<slug:slug>/images/<int:image_id>/delete/',
        views.delete_product_image,
        name='delete_product_image',
    ),
    path('collections/', views.collection_list, name='collection_list'),
    path(
        'collections/<slug:slug>/',
        views.collection_detail,
        name='collection_detail'
    ),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
