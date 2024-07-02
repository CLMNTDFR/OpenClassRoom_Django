# forms.py
from django import forms
from .models import Band, Event, Listing

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
        fields = ('name', 'genre', 'biography', 'official_homepage', 'year_formed', 'active', 'city', 'mail')
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 5}),  # Agrandir la zone de texte pour la biographie
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['band', 'date', 'venue', 'price', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['description', 'type', 'year', 'band', 'point_of_sale', 'sold']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['band'].queryset = Band.objects.all()  # Afficher tous les groupes disponibles dans le formulaire
