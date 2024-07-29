from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.conf import settings
from django.core.exceptions import ValidationError
from PIL import Image

# Validators for image file extension and size
def validate_image_file_extension(value):
    """
    Validate that the uploaded image file has a supported extension.
    """
    valid_extensions = ['JPEG', 'PNG']
    ext = Image.open(value).format
    if ext not in valid_extensions:
        raise ValidationError(
            f'File type not supported. Supported types are: {", ".join(valid_extensions)}')

def validate_image_file_size(value):
    """
    Validate that the uploaded image file size does not exceed 5 MB.
    """
    max_size = 5 * 1024 * 1024  # 5 MB
    if value.size > max_size:
        raise ValidationError(
            f'File too large. Size should not exceed {max_size / 1024 / 1024} MB')

# Model for Band
class Band(models.Model):
    """
    Model representing a musical band.
    """
    class Genre(models.TextChoices):
        METAL = 'Metal', 'Metal'
        BLACK_METAL = 'Black Metal', 'Black Metal'
        DEATH_METAL = 'Death Metal', 'Death Metal'
        THRASH_METAL = 'Thrash Metal', 'Thrash Metal'
        POWER_METAL = 'Power Metal', 'Power Metal'
        PROGRESSIVE_METAL = 'Progressive Metal', 'Progressive Metal'
        SYMPHONIC_METAL = 'Symphonic Metal', 'Symphonic Metal'
        GOTHIC_METAL = 'Gothic Metal', 'Gothic Metal'
        FOLK_METAL = 'Folk Metal', 'Folk Metal'
        VIKING_METAL = 'Viking Metal', 'Viking Metal'
        SLUDGE_METAL = 'Sludge Metal', 'Sludge Metal'
        GROOVE_METAL = 'Groove Metal', 'Groove Metal'
        INDUSTRIAL_METAL = 'Industrial Metal', 'Industrial Metal'
        NU_METAL = 'Nu Metal', 'Nu Metal'
        DJENT = 'Djent', 'Djent'
        HARDCORE = 'Hardcore', 'Hardcore'
        BEATDOWN_HARDCORE = 'Beatdown Hardcore', 'Beatdown Hardcore'
        POST_HARDCORE = 'Post-Hardcore', 'Post-Hardcore'
        MELODIC_HARDCORE = 'Melodic Hardcore', 'Melodic Hardcore'
        HARDCORE_PUNK = 'Hardcore Punk', 'Hardcore Punk'
        CROSSOVER_THRASH = 'Crossover Thrash', 'Crossover Thrash'
        METALCORE = 'Metalcore', 'Metalcore'
        MATHCORE = 'Mathcore', 'Mathcore'
        CRUST_PUNK = 'Crust Punk', 'Crust Punk'
        EXTREME_METAL = 'Extreme Metal', 'Extreme Metal'
        GRINDCORE = 'Grindcore', 'Grindcore'
        BRUTAL_DEATH_METAL = 'Brutal Death Metal', 'Brutal Death Metal'
        TECHNICAL_DEATH_METAL = 'Technical Death Metal', 'Technical Death Metal'
        DEATHGRIND = 'Deathgrind', 'Deathgrind'
        GOREGRIND = 'Goregrind', 'Goregrind'
        PORNOGRIND = 'Pornogrind', 'Pornogrind'
        ALTERNATIVE_AND_FUSION_GENRES = 'Alternative and Fusion Genres', 'Alternative and Fusion Genres'
        ALTERNATIVE_METAL = 'Alternative Metal', 'Alternative Metal'
        AVANT_GARDE_METAL = 'Avant-Garde Metal', 'Avant-Garde Metal'
        FUNK_METAL = 'Funk Metal', 'Funk Metal'
        RAP_METAL = 'Rap Metal', 'Rap Metal'
        JAZZ_METAL = 'Jazz Metal', 'Jazz Metal'
        EXPERIMENTAL_METAL = 'Experimental Metal', 'Experimental Metal'
        DOOM_AND_STONER = 'Doom and Stoner', 'Doom and Stoner'
        TRADITIONAL_DOOM = 'Traditional Doom', 'Traditional Doom'
        FUNERAL_DOOM = 'Funeral Doom', 'Funeral Doom'
        DRONE_DOOM = 'Drone Doom', 'Drone Doom'
        PSYCHEDELIC_DOOM = 'Psychedelic Doom', 'Psychedelic Doom'
        SLUDGE_DOOM = 'Sludge Doom', 'Sludge Doom'
        DESERT_ROCK = 'Desert Rock', 'Desert Rock'
        PUNK_AND_POST_PUNK = 'Punk and Post-Punk', 'Punk and Post-Punk'
        ANARCHO_PUNK = 'Anarcho-Punk', 'Anarcho-Punk'
        SKATE_PUNK = 'Skate Punk', 'Skate Punk'
        POP_PUNK = 'Pop Punk', 'Pop Punk'
        GOTHIC_ROCK = 'Gothic Rock', 'Gothic Rock'
        DEATHROCK = 'Deathrock', 'Deathrock'
        COLDWAVE = 'Coldwave', 'Coldwave'
        NOISE_AND_EXPERIMENTAL = 'Noise and Experimental', 'Noise and Experimental'
        NOISE_ROCK = 'Noise Rock', 'Noise Rock'
        NOISE_PUNK = 'Noise Punk', 'Noise Punk'
        INDUSTRIAL_NOISE = 'Industrial Noise', 'Industrial Noise'
        NOISECORE = 'Noisecore', 'Noisecore'
        POWER_ELECTRONICS = 'Power Electronics', 'Power Electronics'
        EXPERIMENTAL_ROCK = 'Experimental Rock', 'Experimental Rock'
        OTHER_RELATED_STYLES = 'Other Related Styles', 'Other Related Styles'
        GRUNGE = 'Grunge', 'Grunge'
        SHOEGaze = 'Shoegaze', 'Shoegaze'
        POST_ROCK = 'Post-Rock', 'Post-Rock'
        EMO = 'Emo', 'Emo'
        SCREAMO = 'Screamo', 'Screamo'
        POWERVIOLENCE = 'Powerviolence', 'Powerviolence'
        ALTERNATIVE_ROCK = 'Alternative Rock', 'Alternative Rock'

    name = models.CharField(max_length=100)
    genre = models.CharField(choices=Genre.choices, max_length=30, null=True, blank=True)
    biography = models.CharField(max_length=1000, null=True, blank=True)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)],
        null=True, blank=True
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bands', default=1)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='liked_bands', blank=True)
    image = models.ImageField(upload_to='bands/', null=True, blank=True,
                              validators=[validate_image_file_extension, validate_image_file_size])

    audio_file1 = models.FileField(
        upload_to='bands/audio/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])]
    )
    audio_file1_title = models.CharField(max_length=100, null=True, blank=True)

    audio_file2 = models.FileField(
        upload_to='bands/audio/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])]
    )
    audio_file2_title = models.CharField(max_length=100, null=True, blank=True)

    audio_file3 = models.FileField(
        upload_to='bands/audio/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])]
    )
    audio_file3_title = models.CharField(max_length=100, null=True, blank=True)

    def get_first_letter_upper(self):
        """
        Return the first letter of the band's name in uppercase.
        """
        return self.name[0].upper()

    def __str__(self):
        return f'{self.name}'

# Model for Event
class Event(models.Model):
    """
    Model representing a musical event.
    """
    band = models.ForeignKey(
        'Band', related_name='events', on_delete=models.CASCADE)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000, null=True, blank=True)
    event_link = models.URLField(
        max_length=200, null=True, blank=True, verbose_name="Event Link")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events', default=1)

    def __str__(self):
        return f'{self.venue} - {self.date}'

# Model for Listing
class Listing(models.Model):
    """
    Model representing a listing for sale or trade.
    """
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
    point_of_sale = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Point of Sale')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings', default=1)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='liked_listings', blank=True)
    image = models.ImageField(upload_to='listings/', null=True, blank=True,
                              validators=[validate_image_file_extension, validate_image_file_size])

    def __str__(self):
        return f'{self.type} - {self.year}'

# Model for Ad
class Ad(models.Model):
    """
    Model representing an advertisement.
    """
    class Category(models.TextChoices):
        OFFER = 'OF', 'Offer'
        DEMAND = 'DM', 'Demand'

    title = models.CharField(max_length=200)
    category = models.CharField(choices=Category.choices, max_length=2)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Model for Message
class Message(models.Model):
    """
    Model representing a message between users.
    """
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    parent = models.ForeignKey(
        'self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject