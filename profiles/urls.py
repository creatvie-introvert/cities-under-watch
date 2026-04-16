from django.urls import path

from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('orders/', views.profile_orders, name='profile_orders'),
    path('downloads/', views.profile_downloads, name='profile_downloads'),
    path(
        'downloads/<int:download_id>/',
        views.account_download_file,
        name='account_download_file',
    ),
    path('settings/', views.profile_settings, name='profile_settings.html'),
]
