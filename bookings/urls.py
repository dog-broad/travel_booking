# bookings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('travel_options/', views.travel_options, name='travel_options'),
    path('book/<int:travel_id>/', views.book_ticket, name='book_ticket'),
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
