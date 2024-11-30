from django.db import models

from Artify.categories.models import ArtCategory
from Artify.profiles.models import ArtistProfile


class Artwork(models.Model):
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE, related_name='artworks')  # Linked to an artist
    title = models.CharField(max_length=100)  # Title of the artwork
    description = models.TextField(blank=True)  # Optional description
    category = models.ForeignKey(ArtCategory, on_delete=models.SET_NULL, null=True)  # Category of the artwork
    image = models.ImageField(upload_to='artworks/')  # Artwork image
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # Price if it's for sale
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when it was uploaded

    def __str__(self):
        return f"{self.title} by {self.artist.user.username}"

