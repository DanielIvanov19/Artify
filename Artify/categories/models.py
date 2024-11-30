from django.db import models

class ArtCategory(models.Model):
    name = models.CharField(max_length=50)  # Category name
    description = models.TextField(blank=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return self.name

