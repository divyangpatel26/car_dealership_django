# views.py
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

from contacts.models import Contact
from .forms import *
from .models import Account
from django.shortcuts import render, redirect
from cars.models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def register(request):
    return render(request, 'accounts/register.html')


def buyer_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_buyer = True
            user.save()
            messages.success(request, 'You are successfully registered as a buyer')
            return redirect('login')  # Customize the redirect URL
    else:
        form = RegistrationForm()
    return render(request, 'accounts/buyer_registration.html', {'form': form})


def seller_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_seller = True
            user.save()
            messages.success(request, 'You are successfully registered as a seller')
            return redirect('login')  # Customize the redirect URL
    else:
        form = RegistrationForm()
    return render(request, 'accounts/seller_registration.html', {'form': form})


# Login Views
def custom_login(request):
    if request.user.is_authenticated:
        return redirect(dashboard)
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                if user.is_authenticated:
                    if user.is_buyer:
                        login(request, user)
                        return redirect(dashboard)
                    elif user.is_seller:
                        login(request, user)
                        return redirect(dashboard)
        else:
            form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    if user.is_authenticated:
        if user.is_buyer:
            inquiries = Contact.objects.filter(user_id=request.user.id)
            return render(request, 'accounts/buyer_dashboard.html', {'inquiries': inquiries})
        elif user.is_seller:
            user_cars = Car.objects.filter(seller=request.user)
            paginator = Paginator(user_cars, 5)  # Show 10 cars per page
            page = request.GET.get('page')
            try:
                user_cars = paginator.page(page)
            except PageNotAnInteger:
                user_cars = paginator.page(1)
            except EmptyPage:
                user_cars = paginator.page(paginator.num_pages)
    return render(request, 'accounts/seller_dashboard.html', {'user_cars': user_cars})
    return redirect('login')


# logout
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the user's profile page
    else:
      form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


def inquiries(request):
    inquiries = Contact.objects.filter(seller=request.user)
    return render(request, 'accounts/inquiries.html', {'inquiries': inquiries})
