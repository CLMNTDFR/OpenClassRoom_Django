from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from listings.models import Band, Listing, Event, Ad, Message
from listings.forms import ContactUsForm, BandForm, EventForm, ListingForm, AdForm
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import ListView
from django.db.models import Q
from .forms import MessageForm, ReplyForm
from django.contrib.auth import get_user_model

User = get_user_model()

@require_POST
@login_required
def like_band(request, id):
    band = get_object_or_404(Band, id=id)
    user = request.user
    if user in band.likes.all():
        band.likes.remove(user)
        return JsonResponse({'status': 'success', 'action': 'unlike', 'likes': band.likes.count()})
    else:
        band.likes.add(user)
        return JsonResponse({'status': 'success', 'action': 'like', 'likes': band.likes.count()})
    
@require_POST
@login_required
def like_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    user = request.user
    if user in listing.likes.all():
        listing.likes.remove(user)
        return JsonResponse({'status': 'success', 'action': 'unlike', 'likes': listing.likes.count()})
    else:
        listing.likes.add(user)
        return JsonResponse({'status': 'success', 'action': 'like', 'likes': listing.likes.count()})

def home(request):
    ads = Ad.objects.all()  # Récupérer toutes les annonces
    return render(request, 'listings/home.html', {'ads': ads})

def band_list(request):
    bands = Band.objects.all()
    band_groups = {}

    for band in bands:
        first_letter = band.get_first_letter_upper()
        if first_letter not in band_groups:
            band_groups[first_letter] = []
        band_groups[first_letter].append(band)

    sorted_band_groups = dict(sorted(band_groups.items()))

    return render(request, 'listings/band_list.html', {'band_groups': sorted_band_groups})

@login_required
def band_detail(request, id):
    try:
        band = Band.objects.get(id=id)
    except Band.DoesNotExist:
        return HttpResponse('<h1>Sorry, Band not found</h1><h3>Please try again with another ID</h3>', status=404)
    
    return render(request, 'listings/band_detail.html', {'band': band, 'request': request})

@login_required
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES)  # Ajout de request.FILES ici
        if form.is_valid():
            band = form.save(commit=False)
            band.user = request.user  # Définir l'utilisateur actuellement connecté
            band.save()
            messages.success(request, 'Band created successfully!')
            return redirect('band_detail', band.id)
    else:
        form = BandForm()

    return render(request, 'listings/band_form.html', {'form': form, 'request': request})

@login_required
def band_update(request, id):
    band = get_object_or_404(Band, id=id)
    if band.user != request.user:
        return HttpResponse('You are not authorized to update this band.', status=403)

    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES, instance=band)  # Ajout de request.FILES ici
        if form.is_valid():
            form.save()
            return redirect('band_detail', id=band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form, 'band': band, 'request': request})

def listing_list(request):
    listings = Listing.objects.select_related('band').order_by('band__name', 'description')
    listing_groups = {}

    for listing in listings:
        first_letter = listing.band.get_first_letter_upper()
        if first_letter not in listing_groups:
            listing_groups[first_letter] = []
        listing_groups[first_letter].append(listing)

    sorted_listing_groups = dict(sorted(listing_groups.items()))

    return render(request, 'listings/listing_list.html', {'listing_groups': sorted_listing_groups})

@login_required
def listing_detail(request, id):
    try:
        listing = Listing.objects.get(id=id)
    except Listing.DoesNotExist:
        return HttpResponse('<h1>Sorry, Listing not found</h1><h3>Please try again with another ID</h3>', status=404)

    return render(request, 'listings/listing_detail.html', {'listing': listing, 'request': request})

@login_required
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)  # Ajout de request.FILES ici
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user  # Définir l'utilisateur actuellement connecté
            listing.save()
            return redirect('listing_detail', listing.id)
    else:
        form = ListingForm()
    
    return render(request, 'listings/listing_form.html', {'form': form, 'request': request})

@login_required
def listing_update(request, id):
    listing = get_object_or_404(Listing, id=id)
    if listing.user != request.user:
        return HttpResponse('You are not authorized to update this listing.', status=403)

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)  # Ajout de request.FILES ici
        if form.is_valid():
            form.save()
            return redirect('listing_detail', id=listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'form': form, 'listing': listing, 'request': request})

@login_required
def event_list(request):
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')
    past_events = Event.objects.filter(date__lt=now).order_by('-date')
    return render(request, 'listings/event_list.html', {'upcoming_events': upcoming_events, 'past_events': past_events, 'request': request})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Définir l'utilisateur actuellement connecté
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    
    return render(request, 'listings/event_form.html', {'form': form, 'request': request})

@login_required
def event_update(request, id):
    event = get_object_or_404(Event, id=id)
    if event.user != request.user:
        return HttpResponse('You are not authorized to update this event.', status=403)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'listings/event_update.html', {'form': form, 'event': event, 'request': request})

def about(request):
    return render(request, 'listings/about.html', {'request': request})

def listings(request):
    return render(request, 'listings/listings.html', {'request': request})

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

    return render(request, 'listings/contact.html', {'form': form, 'request': request})

@login_required
def band_delete(request, id):
    band = get_object_or_404(Band, id=id)
    if band.user != request.user:
        return HttpResponse('You are not authorized to delete this band.', status=403)

    if request.method == 'POST':
        band.delete()
        messages.success(request, f'The band "{band.name}" has been deleted successfully.', extra_tags='success')
        return redirect('bands_list')
    return render(request, 'listings/band_delete.html', {'band': band, 'request': request})

@login_required
def listing_delete(request, id):
    listing = get_object_or_404(Listing, id=id)
    if listing.user != request.user:
        return HttpResponse('You are not authorized to delete this listing.', status=403)

    if request.method == 'POST':
        listing.delete()
        messages.success(request, f'The listing "{listing.description}" has been deleted successfully.', extra_tags='success')
        return redirect('listing_list')
    return render(request, 'listings/listing_delete.html', {'listing': listing, 'request': request})

@login_required
def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if event.user != request.user:
        return HttpResponse('You are not authorized to delete this event.', status=403)

    if request.method == 'POST':
        event.delete()
        messages.success(request, f'The event "{event.date}" has been deleted successfully.', extra_tags='success')
        return redirect('event_list')
    return render(request, 'listings/event_delete.html', {'event': event, 'request': request})

def privacy_policy(request):
    return render(request, 'listings/privacy_policy.html', {'request': request})

def terms_of_service(request):
    return render(request, 'listings/terms_of_service.html', {'request': request})

@login_required
def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'listings/ad_list.html', {'ads': ads})

@login_required
def ad_detail(request, id):
    ad = get_object_or_404(Ad, id=id)
    return render(request, 'listings/ad_detail.html', {'ad': ad})

@login_required
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('home')
    else:
        form = AdForm()
    return render(request, 'listings/ad_form.html', {'form': form})

def ad_update(request, id):
    ad = get_object_or_404(Ad, id=id)
    if ad.user != request.user:
        return HttpResponse('You are not authorized to update this ad.', status=403)

    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige vers la page d'accueil après la mise à jour
    else:
        form = AdForm(instance=ad)

    return render(request, 'listings/ad_form.html', {'form': form})

@login_required
def ad_delete(request, id):
    ad = get_object_or_404(Ad, id=id)
    if ad.user != request.user:
        return HttpResponse('You are not authorized to delete this ad.', status=403)

    if request.method == 'POST':
        ad.delete()
        return redirect('home')
    return render(request, 'listings/ad_confirm_delete.html', {'ad': ad})

def search(request):
    query = request.GET.get('q')
    if query:
        bands = Band.objects.filter(
            Q(name__icontains=query) | Q(genre__icontains=query)
        )
        listings = Listing.objects.filter(
            Q(description__icontains=query) | Q(band__name__icontains=query) | Q(year__icontains=query)
        )
        events = Event.objects.filter(
            Q(description__icontains=query) | Q(band__name__icontains=query) | Q(venue__icontains=query) | Q(date__icontains=query)
        )
    else:
        bands = Band.objects.none()
        listings = Listing.objects.none()
        events = Event.objects.none()

    return render(request, 'listings/search_results.html', {
        'query': query,
        'bands': bands,
        'listings': listings,
        'events': events,
    })

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_detail', message.id)
    else:
        form = MessageForm()
    return render(request, 'listings/send_message.html', {'form': form})

@login_required
def message_list(request):
    received_messages = Message.objects.filter(recipient=request.user)
    conversations = {}

    for message in received_messages:
        if message.parent is None:
            conversations[message.id] = {
                'message': message,
                'replies': list(Message.objects.filter(parent=message).order_by('-created_at')),
                'last_message': message  # Initialise avec le message principal
            }
        else:
            if message.parent.id not in conversations:
                conversations[message.parent.id] = {
                    'message': message.parent,
                    'replies': [],
                    'last_message': message.parent  # Initialise avec le message principal
                }
            conversations[message.parent.id]['replies'].append(message)
            conversations[message.parent.id]['last_message'] = message  # Met à jour avec le dernier message

    # Récupérer le dernier message de chaque conversation
    for conversation_id, conversation in conversations.items():
        last_message = Message.objects.filter(parent=conversation['message']).order_by('-created_at').first()
        if last_message:
            conversations[conversation_id]['last_message'] = last_message

    # Trier les conversations par la date du dernier message
    sorted_conversations = sorted(conversations.items(), key=lambda x: x[1]['last_message'].created_at, reverse=True)

    return render(request, 'listings/message_list.html', {'conversations': dict(sorted_conversations)})

    # Récupérer le dernier message de chaque conversation
    for conversation_id, conversation in conversations.items():
        last_message = Message.objects.filter(parent=conversation['message']).order_by('-created_at').first()
        if last_message:
            conversations[conversation_id]['last_message'] = last_message

    return render(request, 'listings/message_list.html', {'conversations': conversations})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user not in [message.sender, message.recipient]:
        return render(request, 'authentification/permission_denied.html')
    
    if request.user == message.recipient and not message.read_at:
        message.read_at = timezone.now()
        message.save()
    
    replies = Message.objects.filter(parent=message).order_by('created_at')
    
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.recipient = message.sender
            reply.subject = f"Re: {message.subject}"
            reply.parent = message
            reply.save()
            return redirect('message_detail', message.id)
    else:
        form = ReplyForm()
    
    return render(request, 'listings/message_detail.html', {'message': message, 'replies': replies, 'form': form})

@login_required
def send_message_to_user(request, username):
    recipient = get_object_or_404(User, username=username)
    initial_data = {'recipient': recipient.id}
    if 'subject' in request.GET:
        initial_data['subject'] = request.GET['subject']
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_detail', message.id)
    else:
        form = MessageForm(initial=initial_data)
    return render(request, 'listings/send_message.html', {'form': form, 'recipient': recipient})

@require_GET
@login_required
def check_unread_messages(request, user_id):
    print(f"Checking unread messages for user {user_id}")
    has_unread_messages = Message.objects.filter(recipient_id=user_id, read_at__isnull=True).exists()
    print(f"Has unread messages: {has_unread_messages}")
    return JsonResponse({'has_unread_messages': has_unread_messages})