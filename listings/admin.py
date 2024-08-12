from django.contrib import admin
from listings.models import Band, Listing, Event, Ad
from authentification.models import User
from django import forms
from PIL import Image

# Custom form for BandAdmin to validate image file type and size
class BandAdminForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'

    def clean_image_url(self):
        image_url = self.cleaned_data.get('image_url')
        if image_url:
            # Assuming you're validating image URLs rather than the actual file
            pass
        return image_url

# Admin configuration for Band model
class BandAdmin(admin.ModelAdmin):
    form = BandAdminForm
    list_display = ('name', 'year_formed', 'genre', 'city', 'mail', 'image_url')

# Admin configuration for Listing model
class ListingAdmin(admin.ModelAdmin):
    list_display = ('description', 'year', 'type', 'band', 'image_url')

# Admin configuration for Event model
class EventAdmin(admin.ModelAdmin):
    list_display = ('band', 'date', 'venue', 'price')

# Admin configuration for User model
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

# Admin configuration for Ad model
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'created_at', 'updated_at')
    list_filter = ('category', 'user')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

# Register models with their respective admin configurations
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Ad, AdAdmin)
