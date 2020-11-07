
from django.contrib import admin
from home.models import Friend
from .models import Contact, Privacy , Terms


# Register your models here.
admin.site.register(Friend)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','content','user']
admin.site.register(Contact, ContactAdmin)


class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Privacy, PrivacyAdmin)


class TermsAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Terms, TermsAdmin)