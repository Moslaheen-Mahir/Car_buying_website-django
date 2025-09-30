from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('profile/', views.profilepage, name='profile'),
    path('logout/', views.logoutpage, name='logout'), 
    path('change_password/', views.change_passwordpage, name='change_password'), 
    path('user_dashboard/', views.user_dashboardpage, name='user_dashboard'), 
    # path('admin_dashboard/', views.admin_dashboardpage, name='admin_dashboard'), 
    path('wishlist/', views.wishlistpage, name='wishlist'),
    path('wishlist/add/<slug:car_slug>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<slug:car_slug>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]