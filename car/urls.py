from django.urls import path
from . import views
urlpatterns = [
    path('our_cars/', views.our_carspage, name='our_cars'),
    path('<slug:car_slug>/', views.car_detailpage, name='car_detail'),
]
