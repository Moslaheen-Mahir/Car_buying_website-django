from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Car(models.Model):
    car_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Car_images/')
    image_2 = models.ImageField(upload_to='Car_images/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.car_name)
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.car_name