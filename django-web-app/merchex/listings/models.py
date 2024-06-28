from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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

class Title(models.Model):
    name = models.CharField(max_length=100)

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