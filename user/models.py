from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    costumer =models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20,null=True)
    image = models.ImageField(default='avatar.jpg',upload_to='profile_images')

    def __str__(self):
        return f'{self.costumer.username}-profile'
