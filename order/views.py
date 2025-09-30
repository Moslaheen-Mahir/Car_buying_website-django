from django.shortcuts import render, get_object_or_404, redirect
from car.models import Car
from .models import Order

# Create your views here.
def placing_order(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()
        card_name = request.POST.get("card_name", "").strip()
        card_number = request.POST.get("card_number", "").strip()
        expiry = request.POST.get("expiry", "").strip()
        cvv = request.POST.get("cvv", "").strip()

        if full_name and email and phone and address:
            Order.objects.create(
                car=car,
                user=request.user,
                full_name=full_name,
                email=email,
                phone=phone,
                address=address,
                card_name=card_name,
                card_number=card_number,
                expiry=expiry,
                cvv=cvv,
                status="Pending",
            )
            return redirect("order_success")
        else:
            context = {
                "car": car,
                "error": "Please fill in all required fields."
            }
            return render(request, "order/placing_order.html", context)

    return render(request, "order/placing_order.html", {"car": car})

def order_success(request):
    return render(request, 'order/order_success.html')
