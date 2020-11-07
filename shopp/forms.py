from django import forms
from login.models import User
from .models import Product



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class ShopCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    

    class Meta:
        #model = Shop
        fields = (
            'shop_name',
            'shop_contact',
            'last_name',
            ' shop_email',
            
        )
    def save(self, commit=True):
        User = super(ShopCreationForm, self).save(commit=False)
        User.shop_name = self.cleaned_data['first_name']
        User.shop_name = self.cleaned_data['last_name']
        User.shop_email = self.cleaned_data['email']

        if commit:
            User.save()

        return User



class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        
        
        fields = [
            'category',
            'name',
            'slug', 
            'image',
            'image2',
            'image3',
            'description',
            'price',
            'stock',
            'available',
            
           
        ]

        
    def save(self, user=None):
        product = super(ProductForm, self).save(commit=False)
        if user:
            product.user = user
        product.save()
        return product

