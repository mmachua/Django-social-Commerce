from django.contrib import admin
from .models import Category, Product ,Shop
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display =['name','slug','user']
    prepopulated_fields = {'slug': ('name','user')}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created','updated','user']
    list_filter = ['available', 'created', 'updated', 'category']
    prepopulated_fields = {'slug': ('name','user')}
admin.site.register(Product, ProductAdmin)
 
