"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views
import authentification.views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', authentification.views.login_page, name='login'),
    path('logout/', authentification.views.logout_user, name='logout'),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('account/<str:username>/', authentification.views.account_view, name='account'),
    path('account/<str:username>/edit/', authentification.views.edit_account, name='edit_account'),
    path('account/<str:username>/delete/', authentification.views.delete_account, name='delete_account'),
    path('bands/', views.band_list, name='bands_list'),
    path('bands/<int:id>/', views.band_detail, name='band_detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/change/', views.band_update, name='band-update'),
    path('about/', views.about, name='about'),
    path('merch/', views.listing_list, name='listing_list'),
    path('merch/<int:id>/', views.listing_detail, name='listing_detail'),
    path('merch/add/', views.listing_create, name='listing_create'),
    path('merch/<int:id>/change/', views.listing_update, name='listing-update'),
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:id>/change/', views.event_update, name='event-update'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),
    path('merch/<int:id>/delete/', views.listing_delete, name='listing-delete'),
    path('events/<int:id>/delete/', views.event_delete, name='event-delete'),
]