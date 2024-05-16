# rentscraper/models.py

from django.db import models

class RentalListing(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    full_url = models.URLField(max_length=500)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    image_urls = models.TextField()
    price = models.CharField(max_length=100)
    bedrooms = models.CharField(max_length=50)  # Changed to CharField to handle non-numeric values
    baths = models.FloatField()
    size = models.CharField(max_length=100)
    HeatIncluded = models.BooleanField(default=False)
    HotWaterIncluded = models.BooleanField(default=False)
    CatAllowed = models.BooleanField(default=False)
    DogAllowed = models.BooleanField(default=False)
    Balcony = models.BooleanField(default=False)
    InBuildingLaundry = models.BooleanField(default=False)
    ParkingAvailable = models.BooleanField(default=False)
    GymAvailable = models.BooleanField(default=False)

    def __str__(self):
        return self.title
