from django.test import TestCase, Client
from django.urls import reverse
from listings.models import Band, Listing, Ad, Event
from django.contrib.auth import get_user_model

# Test for "band" model
class BandModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        Band.objects.create(name="Test Band", genre="Rock", year_formed=2020, user=self.user)

    def test_band_name(self):
        band = Band.objects.get(name="Test Band")
        self.assertEqual(band.name, "Test Band")

    def test_band_genre(self):
        band = Band.objects.get(name="Test Band")
        self.assertEqual(band.genre, "Rock")

    def test_band_year_formed(self):
        band = Band.objects.get(name="Test Band")
        self.assertEqual(band.year_formed, 2020)

# Test for "band" view
class BandListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        Band.objects.create(name="Test Band", genre="Rock", year_formed=2020, user=self.user)

    def test_band_list_view(self):
        response = self.client.get(reverse('bands_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Band")
        self.assertTemplateUsed(response, 'listings/band_list.html')

# Test for "listing" model
class ListingModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.band = Band.objects.create(name="Test Band", genre="Rock", year_formed=2020, user=self.user)
        Listing.objects.create(description="Test Listing", year=2020, type="Records", band=self.band, user=self.user)

    def test_listing_description(self):
        listing = Listing.objects.get(description="Test Listing")
        self.assertEqual(listing.description, "Test Listing")

    def test_listing_year(self):
        listing = Listing.objects.get(description="Test Listing")
        self.assertEqual(listing.year, 2020)

    def test_listing_type(self):
        listing = Listing.objects.get(description="Test Listing")
        self.assertEqual(listing.type, "Records")

# Test for "listing" view
class ListingListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.band = Band.objects.create(name="Test Band", genre="Rock", year_formed=2020, user=self.user)
        Listing.objects.create(description="Test Listing", year=2020, type="Records", band=self.band, user=self.user)

    def test_listing_list_view(self):
        response = self.client.get(reverse('listing_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Listing")
        self.assertTemplateUsed(response, 'listings/listing_list.html')

# Test for "ad" model
class AdModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        Ad.objects.create(title="Test Ad", category="OF", description="This is a test ad.", user=self.user)

    def test_ad_title(self):
        ad = Ad.objects.get(title="Test Ad")
        self.assertEqual(ad.title, "Test Ad")

    def test_ad_category(self):
        ad = Ad.objects.get(title="Test Ad")
        self.assertEqual(ad.category, "OF")

    def test_ad_description(self):
        ad = Ad.objects.get(title="Test Ad")
        self.assertEqual(ad.description, "This is a test ad.")

# Test for "ad" view
class AdListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        Ad.objects.create(title="Test Ad", category="OF", description="This is a test ad.", user=self.user)

# Test for "Event" model
class EventModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.band = Band.objects.create(name="Test Band", genre="Rock", year_formed=2020, user=self.user)
        Event.objects.create(band=self.band, date="2024-01-01", venue="Test Venue", price=100.00, user=self.user)

    def test_event_date(self):
        event = Event.objects.get(venue="Test Venue")
        self.assertEqual(event.date.strftime('%Y-%m-%d'), "2024-01-01")

    def test_event_venue(self):
        event = Event.objects.get(venue="Test Venue")
        self.assertEqual(event.venue, "Test Venue")

    def test_event_price(self):
        event = Event.objects.get(venue="Test Venue")
        self.assertEqual(event.price, 100.00)

# Test for "event" view
class EventListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.band = Band.objects.create(name="Test Band", genre="Rock", year_formed=2020, user=self.user)
        Event.objects.create(band=self.band, date="2024-01-01", venue="Test Venue", price=100.00, user=self.user)
