from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from car.models import Car
from order.models import Order
from .models import Wishlist

# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
        
    return render(request, 'account/login.html')

def registerpage(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'account/register.html', {'form': form})

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required
def profilepage(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'account/profile.html', {'form': form})

@login_required
def change_passwordpage(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Keep the user logged in after changing password
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'account/change_password.html', {'form': form})

@login_required
def user_dashboardpage(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    # return render(request, 'account/dashboard.html')
    return render(request, 'account/dashboard.html', {'orders': orders})

# def admin_dashboardpage(request):
#     if not request.user.is_staff:
#         return redirect('user_dashboard')
#     cars = Car.objects.all()
#     orders = Order.objects.all()
#     return render(request, 'account/admin_dashboard.html')
    # return render(request, 'account/admin_dashboard.html', {'cars': cars, 'orders': orders})
    
@login_required
def wishlistpage(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'account/wishlist.html', {'wishlist': [item.car for item in wishlist_items]})

@login_required
def add_to_wishlist(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    Wishlist.objects.get_or_create(user=request.user, car=car)
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    Wishlist.objects.filter(user=request.user, car=car).delete()
    return redirect('wishlist')