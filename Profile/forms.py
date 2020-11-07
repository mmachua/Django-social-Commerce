from django import forms
from login.models import User, Shop, Client
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#the models for these forms are in login.// rhis form has been put here as an extension
class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop

        fields = [
            
            'shop_name',
            'description',
            'city',
            'website',
            'phone',
            'image'
        ]

    def save(self, user=None):
        shop = super(ShopForm, self).save(commit=False)
        if user:
            shop.user = user
        shop.save()
        return shop




class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
       # model = User

        fields = [
            
            'phone',
            'city',
            'image',
            'gender',
            
        ]

    def save(self, user=None):
        client = super(ClientForm, self).save(commit=False)
        if user:
            client.user = user
        client.save()
        return client





#    def save(self, commit=True):
#        Client = super(ClientForm, self).save(commit=False)
#        Client.phone = self.cleaned_data['phone']
#        Client.image = self.cleaned_data['image']
#        Client.city = self.cleaned_data['city']
#        Client.gender = self.cleaned_data['gender']

#        if commit:
 #           Client.save()

#        return Client


