from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from listings.models import Band, Listing, Event
from listings.forms import ContactUsForm, BandForm, EventForm, ListingForm
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone

def home(request):
    return render(request, 'listings/home.html')

def band_list(request):
    bands = Band.objects.order_by('name')
    alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    return render(request, 'listings/band_list.html', {'bands': bands, 'alphabet': alphabet})

def band_detail(request, id):
    try:
        band = Band.objects.get(id=id)
    except Band.DoesNotExist:
        return HttpResponse('<h1>Sorry, Band not found</h1><h3>Please try again with another ID</h3>', status=404)
    
    return render(request, 'listings/band_detail.html', {'band': band})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Band created successfully!')
            return redirect('band_detail', form.instance.id)
    else:
        form = BandForm()

    return render(request, 'listings/band_form.html', {'form': form})

def band_update(request, id):
    band = get_object_or_404(Band, id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band_detail', id=band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form, 'band': band})

def listing_list(request):
    listings = Listing.objects.select_related('band').order_by('band__name', 'description')
    alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    return render(request, 'listings/listing_list.html', {'listings': listings, 'alphabet': alphabet})

def listing_detail(request, id):
    try:
        listing = Listing.objects.get(id=id)
    except Listing.DoesNotExist:
        return HttpResponse('<h1>Sorry, Listing not found</h1><h3>Please try again with another ID</h3>', status=404)

    return render(request, 'listings/listing_detail.html', {'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', form.instance.id)
    else:
        form = ListingForm()
    
    return render(request, 'listings/listing_form.html', {'form': form})

def listing_update(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', id=listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'form': form, 'listing': listing})

def event_list(request):
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')
    past_events = Event.objects.filter(date__lt=now).order_by('-date')
    return render(request, 'listings/event_list.html', {'upcoming_events': upcoming_events, 'past_events': past_events})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    
    return render(request, 'listings/event_form.html', {'form': form})

def event_update(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'listings/event_update.html', {'form': form, 'event': event})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    return render(request, 'listings/listings.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via NUB Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['deferclement59@gmail.com'],
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})

def band_delete(request, id):
    band = get_object_or_404(Band, id=id)
    if request.method == 'POST':
        band.delete()
        messages.success(request, f'The band "{band.name}" has been deleted successfully.', extra_tags='success')
        return redirect('band_list')
    return render(request, 'listings/band_delete.html', {'band': band})

def listing_delete(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        listing.delete()
        messages.success(request, f'The listing "{listing.description}" has been deleted successfully.', extra_tags='success')
        return redirect('listing_list')
    return render(request, 'listings/listing_delete.html', {'listing': listing})

def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, f'The event "{event.name}" has been deleted successfully.', extra_tags='success')
        return redirect('event_list')
    return render(request, 'listings/event_delete.html', {'event': event})

def privacy_policy(request):
    return render(request, 'listings/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'listings/terms_of_service.html')