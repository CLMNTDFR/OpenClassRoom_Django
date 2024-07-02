from django.contrib import admin
from listings.models import Band, Listing, Event

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'city', 'mail')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('description', 'sold', 'year', 'type', 'band')

class EventAdmin(admin.ModelAdmin):
    list_display = ('band', 'date', 'venue', 'price')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Event, EventAdmin)
