from django.contrib.auth import get_user_model
from django.db import models
from Artify.profiles.models import Artist


UserModel = get_user_model()

class CustomerOrder(models.Model):
    CATEGORY_CHOICES = [
        ('tshirt', 'T-Shirt'),
        ('canvas', 'Canvas'),
        ('accessories', 'Accessories'),
    ]

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # Linked to the user who made the order
    order_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
    )
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)  # Select an artist
    design_details = models.TextField(help_text="Details about the desired design")
    image = models.ImageField(upload_to='order_images/', blank=True, null=True)  # Upload image
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price of the order
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

