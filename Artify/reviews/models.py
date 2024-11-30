from django.db import models

from Artify.artworks.models import Artwork
from Artify.orders.models import CustomerOrder


class Review(models.Model):
    RATINGS = [(i, str(i)) for i in range(1, 6)]  # 1-5 star rating system

    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviews')  # Customer who wrote the review
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)  # Artwork being reviewed (optional)
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)  # Order being reviewed (optional)
    content = models.TextField()  # Review content
    rating = models.IntegerField(choices=RATINGS)  # Rating out of 5
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"Review by {self.customer.username} ({self.rating} Stars)"

