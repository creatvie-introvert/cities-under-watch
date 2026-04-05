from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('collections/', views.collection_list, name='collection_list'),
    path(
        'collections/<slug:slug>/',
        views.collection_detail,
        name='collection_detail'
    ),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
