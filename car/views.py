from django.shortcuts import render, get_object_or_404
from car.models import Car
from django.core.paginator import Paginator
# Create your views here.

def our_carspage(request):
    cars = Car.objects.filter(is_available=True).order_by('-id')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    for car in paged_cars:
        print(car)
    return render(request, 'car/our_cars.html', {'cars':paged_cars})

def car_detailpage(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    return render(request, 'car/car_detail.html', {'car': car})