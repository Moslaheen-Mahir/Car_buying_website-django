from django.urls import path
from . import views
urlpatterns = [
    path('placing_order/<slug:car_slug>/', views.placing_order, name='placing_order'),
    path('order_success/', views.order_success, name='order_success'),
]
