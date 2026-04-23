from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms_and_conditions, name='terms_and_conditions'),
    path('refunds/', views.refund_policy, name='refund_policy'),
    path('delivery/', views.delivery_policy, name='delivery_policy'),
    path(
        'newsletter-subscribe/',
        views.newsletter_subscribe,
        name='newsletter_subscribe',
    ),
]
