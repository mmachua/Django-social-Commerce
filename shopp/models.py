from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from login.models import Shop , Client
from login.models import User


#models for category
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name='category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_re_path(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

def __str__(self):
    return self.user.bizname
#end model category

#product models
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=False)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description =models.TextField(blank=True, max_length=1301)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
 
    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


    def get_delete_re_path(self):
        return "/Profile/delete/".format(self.id)
    

    def get_absolute_re_path(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
#end product models

