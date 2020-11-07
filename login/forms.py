from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth import get_user_model
from login.models import User, Client, Shop


class ClientSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
        
        @transaction.atomic
        def save(self, commit=True):
            user = super(ClientSignUpForm, self).save(commit=False)
            User.username = self.cleaned_data['username']
            User.email = self.cleaned_data['email']
            user.is_client = True
            if commit:
                user.save()
            return user



class ShopSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

        def save(self, commit=True):
            user = super(ShopSignUpForm, self).save(commit=True)
            User.username = self.cleaned_data['username']
            User.email = self.cleaned_data['email']
            user.is_shop = True
            if commit:
                user.save()
            return user



class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        )


class EditShopForm(UserChangeForm):

    class Meta:
        #model = EditShopForm
        fields = (
            'shop_name',
            'description',
            'image',
            'city',
            'phone',
            'website'

        )