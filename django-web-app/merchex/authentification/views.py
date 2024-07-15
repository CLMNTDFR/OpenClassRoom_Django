from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . import forms
from .forms import SignupForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import User
from listings.models import Band, Event, Listing  # Import des modèles depuis l'application listings

def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('account', username=user.username)
    return render(request, 'authentification/signup.html', context={'form': form})

@login_required
def account_view(request, username):
    user = get_object_or_404(User, username=username)
    if user != request.user:
        # Si l'utilisateur n'est pas celui connecté, rediriger vers une page d'erreur ou de permission refusée
        return render(request, 'authentification/permission_denied.html')
    
    # Récupérer les items créés par l'utilisateur
    bands = Band.objects.filter(user=user)
    events = Event.objects.filter(user=user)
    listings = Listing.objects.filter(user=user)
    
    return render(request, 'authentification/account.html', {'user': user, 'bands': bands, 'events': events, 'listings': listings})

def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials.')
    return render(
        request, 'authentification/login.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def edit_account(request, username):
    user = get_object_or_404(User, username=username)
    if user != request.user:
        return render(request, 'authentification/permission_denied.html')
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)  # Ajout de request.FILES ici
        if form.is_valid():
            form.save()
            return redirect('account', username=user.username)
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'authentification/edit_account.html', {'form': form})

@login_required
def delete_account(request, username):
    user = get_object_or_404(User, username=username)
    if user != request.user:
        return render(request, 'authentification/permission_denied.html')
    if request.method == 'POST':
        user.delete()
        logout(request)
        return redirect('home')
    return render(request, 'authentification/confirm_delete.html', {'user': user})
