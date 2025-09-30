from django.db import models
from django.contrib.auth.models import User
from car.models import Car

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'car')  # Prevent duplicates

    def __str__(self):
        return f"{self.user.username} - {self.car.car_name}"
