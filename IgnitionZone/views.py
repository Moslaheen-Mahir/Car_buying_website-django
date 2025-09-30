from django.shortcuts import render
from car.models import Car
def homeview(request):
    latest_cars = Car.objects.filter(is_available=True).order_by('-id')[:3]
    return render(request, 'index.html', {'latest_cars': latest_cars})

def aboutview(request):
    return render(request, 'about.html')