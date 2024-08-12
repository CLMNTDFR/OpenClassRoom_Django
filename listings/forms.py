from django import forms
from .models import Band, Event, Listing, Ad, Message

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}), max_length=2000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'genre', 'biography', 'year_formed', 'active', 'official_homepage', 'city', 'mail', 'image_url', 'audio_file1', 'audio_file1_title', 'audio_file2', 'audio_file2_title', 'audio_file3', 'audio_file3_title']
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 5}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'audio_file1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'audio_file1_title': forms.TextInput(attrs={'class': 'form-control'}),
            'audio_file2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'audio_file2_title': forms.TextInput(attrs={'class': 'form-control'}),
            'audio_file3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'audio_file3_title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['band', 'date', 'venue', 'price', 'description', 'event_link']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['description', 'type', 'year', 'band', 'point_of_sale', 'image_url']
        widgets = {
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'image_url': 'Image URL',
        }
        help_texts = {
            'image_url': 'Host your image on a service like https://postimages.org/ and paste the URL here.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['band'].queryset = Band.objects.all()

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'category', 'description']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body', 'parent']
        widgets = {
            'recipient': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'parent': forms.HiddenInput(),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
