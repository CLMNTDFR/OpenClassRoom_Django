from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Title


def hello(request):
    bands = Band.objects.all()
    titles = Title.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands, 'titles': titles})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    return render(request, 'listings/listings.html')

def contact(request):
    return render(request, 'listings/contact.html')
