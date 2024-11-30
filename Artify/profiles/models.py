from django.db import models

from Artify.categories.models import ArtCategory


class ArtistProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Linked to Django's User model
    bio = models.TextField(blank=True)  # Bio for the artist
    profile_picture = models.ImageField(upload_to='artist_profiles/', blank=True, null=True)  # Profile picture
    specialties = models.ManyToManyField(ArtCategory, related_name='artists')  # Areas of expertise

    def __str__(self):
        return f"{self.user.username}'s Profile"

