from django.contrib import admin
from listings.models import Band, Listing, Event
from authentification.models import User

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'city', 'mail')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('description', 'sold', 'year', 'type', 'band')

class EventAdmin(admin.ModelAdmin):
    list_display = ('band', 'date', 'venue', 'price')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(User, UserAdmin)
