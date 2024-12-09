from django.db import models
from Artify.profiles.models import Artist


class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)  # Optional artist
    title = models.CharField(max_length=100)  # Title of the artwork
    description = models.TextField(blank=True)  # Optional description
    image = models.ImageField(upload_to='artworks/')  # Artwork image
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # Price if it's for sale

    def __str__(self):
        return f"{self.title} by {self.artist.user.username}"

