from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils import timezone
from martinn import settings
from django.db.models.signals import post_save

class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    is_shop = models.BooleanField(default=False)


class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=21, default='')
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True, default='0')

    def __str__(self):
        return self.user.username


class Client(models.Model):
    
    phone = models.IntegerField(default=0)
    city = models.CharField(max_length=100,blank=True, null=True, default='',choices=(
                                    ('Nairobi', 'Nairobi'),  
                                    ('Nakuru', 'Nakuru')))
    image = models.ImageField(upload_to='profile_image', blank=False ,default='')
    gender = models.CharField(max_length=6,blank=True, null=True, default='',choices=(
                                    ('M', 'Male'),  
                                    ('F', 'Female')))
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

