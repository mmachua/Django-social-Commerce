from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


from login.decorators import client_required, shop_required
from login.models import Shop, User
from django.views.generic import TemplateView , CreateView
from login.forms import ShopSignUpForm


class ShopSignUpView(CreateView):
    template_name = 'registration/signup_form.html'
    model = Shop
    form_class = ShopSignUpForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'shop'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('shop:product_list')



