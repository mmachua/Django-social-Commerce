
from __future__ import unicode_literals
from django.db import models
from login.models import User
from login.models import Shop, Client
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse



#this model help in storing and remooving favourite shops
class Friend(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name="owner", null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend,created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)
    
    def __str__(self):
        return str(self.current_user)

    def user(self):
        return self.users.count()

#end view

#contact mmodel helps clients and shops to contact Favourite
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    content = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#privacy model
class Privacy(models.Model):
    title = models.CharField(max_length=55, default='')
    text = models.TextField(max_length=7000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Terms(models.Model):
    title = models.CharField(max_length=55, default='')
    text = models.TextField(max_length=100000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title