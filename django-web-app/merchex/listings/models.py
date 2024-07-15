from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.core.exceptions import ValidationError
from PIL import Image

def validate_image_file_extension(value):
    valid_extensions = ['JPEG', 'PNG']
    ext = Image.open(value).format
    if ext not in valid_extensions:
        raise ValidationError(f'File type not supported. Supported types are: {", ".join(valid_extensions)}')

def validate_image_file_size(value):
    max_size = 5 * 1024 * 1024  # 5 Mo
    if value.size > max_size:
        raise ValidationError(f'File too large. Size should not exceed {max_size / 1024 / 1024} MB')

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

    name = models.CharField(max_length=100)
    genre = models.CharField(choices=Genre.choices, max_length=20, null=True, blank=True)
    biography = models.CharField(max_length=1000, null=True, blank=True)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)],
        null=True, blank=True
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bands', default=1)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_bands', blank=True)
    image = models.ImageField(upload_to='bands/', null=True, blank=True, validators=[validate_image_file_extension, validate_image_file_size])

    def __str__(self):
        return f'{self.name}'

class Event(models.Model):
    band = models.ForeignKey('Band', related_name='events', on_delete=models.CASCADE)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000, null=True, blank=True)
    event_link = models.URLField(max_length=200, null=True, blank=True, verbose_name="Event Link")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events', default=1)

    def __str__(self):
        return f'{self.venue} - {self.date}'

class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'Records', 'Records'
        CLOTHING = 'Clothing', 'Clothing'
        POSTERS = 'Posters', 'Posters'
        MISCELLANEOUS = 'Miscellaneous', 'Miscellaneous'

    description = models.CharField(max_length=1000, null=True, blank=True)
    sold = models.BooleanField(default=False, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    type = models.CharField(choices=Type.choices, max_length=20, null=True, blank=True)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    point_of_sale = models.CharField(max_length=255, null=True, blank=True, verbose_name='Point of Sale')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings', default=1)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_listings', blank=True)
    image = models.ImageField(upload_to='listings/', null=True, blank=True, validators=[validate_image_file_extension, validate_image_file_size])

    def __str__(self):
        return f'{self.type} - {self.year}'

class Ad(models.Model):
    class Category(models.TextChoices):
        OFFER = 'OF', 'Offer'
        DEMAND = 'DM', 'Demand'

    title = models.CharField(max_length=200)
    category = models.CharField(choices=Category.choices, max_length=2)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title