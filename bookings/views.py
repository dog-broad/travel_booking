# bookings/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import TravelOption, Booking
from .forms import UserRegistrationForm, UserUpdateForm, BookingForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('travel_options')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('travel_options')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('landing')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    # Fetch booking history
    bookings = Booking.objects.filter(user=request.user)
    
    # Render the profile page with form and booking history
    return render(request, 'profile.html', {'form': form, 'bookings': bookings})

@login_required
def book_ticket(request, travel_id):
    travel_option = get_object_or_404(TravelOption, pk=travel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel_option
            booking.total_price = booking.number_of_seats * travel_option.price
            booking.save()
            travel_option.available_seats -= booking.number_of_seats
            travel_option.save()
            return redirect('view_bookings')
    else:
        form = BookingForm()
    return render(request, 'book_ticket.html', {'form': form, 'travel_option': travel_option})

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'view_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    booking.status = 'Cancelled'
    booking.save()
    travel_option = booking.travel_option
    travel_option.available_seats += booking.number_of_seats
    travel_option.save()
    return redirect('view_bookings')

def landing(request):
    return render(request, 'landing.html')
