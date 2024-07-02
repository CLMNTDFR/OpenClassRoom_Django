from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import URLValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH', 'Hip Hop'
        SYNTH_POP = 'SP', 'Synth Pop'
        ALTERNATIVE_ROCK = 'AR', 'Alternative Rock'
        POP = 'POP', 'Pop'
        ROCK = 'ROCK', 'Rock'
        JAZZ = 'JAZZ', 'Jazz'
        BLUES = 'BLUES', 'Blues'
        ELECTRONIC = 'ELECTRONIC', 'Electronic'
        FOLK = 'FOLK', 'Folk'
        COUNTRY = 'COUNTRY', 'Country'
        REGGAE = 'REGGAE', 'Reggae'
        CLASSICAL = 'CLASSICAL', 'Classical'
        METAL = 'METAL', 'Metal'
        PUNK = 'PUNK', 'Punk'
        R_AND_B = 'R_AND_B', 'R&B'
        SOUL = 'SOUL', 'Soul'
        FUNK = 'FUNK', 'Funk'
        DISCO = 'DISCO', 'Disco'
        LATIN = 'LATIN', 'Latin'
        WORLD = 'WORLD', 'World'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=20, null=True, blank=True)
    biography = models.fields.CharField(max_length=1000, null=True, blank=True)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)],
        null=True, blank=True
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    city = models.fields.CharField(max_length=100, null=True, blank=True)
    mail = models.fields.EmailField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Event(models.Model):
    band = models.ForeignKey('Band', related_name='events', on_delete=models.CASCADE)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000, null=True, blank=True)
    event_link = models.URLField(max_length=200, null=True, blank=True, verbose_name="Event Link")

    def __str__(self):
        return f'{self.venue} - {self.date}'

class Listing(models.Model):

    class Type(models.TextChoices):
        RECORDS = 'Records', 'Records'
        CLOTHING = 'Clothing', 'Clothing'
        POSTERS = 'Posters', 'Posters'
        MISCELLANEOUS = 'Miscellaneous', 'Miscellaneous'

    description = models.fields.CharField(max_length=1000, null=True, blank=True)
    sold = models.fields.BooleanField(default=False, null=True, blank=True)
    year = models.fields.IntegerField(null=True, blank=True)
    type = models.fields.CharField(choices=Type.choices, max_length=20, null=True, blank=True)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    point_of_sale = models.CharField(max_length=255, null=True, blank=True, verbose_name='Point of Sale')


    def __str__(self):
        return f'{self.type} - {self.year}'
