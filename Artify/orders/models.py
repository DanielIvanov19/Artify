from django.db import models
from django.contrib.auth.models import User



class CustomerOrder(models.Model):
    CATEGORY_CHOICES = [
        ('TShirt', 'T-Shirt'),
        ('Accessory', 'Accessory'),
        ('Canvas', 'Canvas'),
    ]

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Linked to the user who made the order
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # What kind of order it is
    description = models.TextField()  # Order details
    image = models.ImageField(upload_to='order_images/', blank=True, null=True)  # Upload image
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price of the order
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of order creation

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} ({self.category})"

