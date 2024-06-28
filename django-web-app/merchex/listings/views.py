from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    band_list = "\n".join([f'<li>{band.name}</li>' for band in bands])
    return HttpResponse(f"""
                        <h1>Hello Django!</h1>
                        <p>Here are the bands:</p>
                        <ul>
                            {band_list}
                        </ul>
""")

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>Merchex is a platform for buying and selling merchandise.</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Here are the listings of merchandise.</p>')

def contact(request):
    return HttpResponse('<h1>Contact-us</h1> <p>Contact us to have more information about our platform.</p>')
