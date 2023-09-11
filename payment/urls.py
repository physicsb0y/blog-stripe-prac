from django.urls import path
from . import views
from .views import HomePageView

import stripe

# app_name="payment"
urlpatterns = [
    path('', HomePageView.as_view(), name='payment_home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('payment-detail', views.pricing_page, name='pricing_page')
]
