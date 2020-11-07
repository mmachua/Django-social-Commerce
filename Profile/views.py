from django.views.generic import TemplateView
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from login.models import User, Client, Shop
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView, UpdateView, CreateView, FormView, DeleteView)
from django.utils.decorators import method_decorator
from shopp.models import Product, Category, Shop
from django.core.paginator import Paginator
from Profile.models import About
from types import MethodType
from operator import attrgetter
from shopp.forms import ProductForm
from Profile.forms import ShopForm, ClientForm
from login.decorators import shop_required, client_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from home.models import Friend
from django.urls import reverse_lazy 
from random import randint
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist


#this is the view that helps users to view shops either theirs or others!!! it has pk that diffrentiates between the two
class ProfileView(TemplateView):
    template_name = 'Profile/Profile.html'
    
    def get(self, request, category_slug=None, pk=None):
        category = None
        context = {}

        if pk:
            category = None
            user = User.objects.get(pk=pk)
            products = Product.objects.filter(user=user).order_by('-updated')
            category = Category.objects.filter(user=user)
            
        else:
            category = None
            user = request.user
            products = Product.objects.filter(user=request.user.id).order_by('-updated')
            category = Category.objects.filter(user=request.user.id)


        paginator = Paginator(products,28)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        index = products.number -1
        max_index = len(paginator.page_range)
        start_index = index -5 if index >= 5 else 0 
        end_index = index + 5 if index <=max_index  -5 else max_index
        page_range = paginator.page_range[start_index:end_index]

   
        args = { 
                 'user' : user,
                  'products' : products, 'category' : category,
                  'page_range':page_range
                 
        }
        return render(request, self.template_name, args)

#end view 

#about view
class AboutView(TemplateView):
    template_name = 'Profile/about.html'

    def get(self, request):
        about = About.objects.all()
        
        args = {'about': about}
        return render(request, self.template_name, args)

#end about
 
#view that shows favourite shops
def favouriteshops(request):

    try:
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except:
        users = User.objects.all()
        friends = print("no favourites!!!")

    return render (request, 'Profile/favourites.html', {'users':users,'friends': friends  })

#end view

#view that shows all  shops, this view was originally a class but changed to accomodate pagination which later should be returned to a class
@login_required
def shop(request):

    try:

        users = User.objects.exclude(id=request.user.id).order_by('-last_login')
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

    except:
        users = User.objects.all().order_by('-last_login')
        friends = Friend.objects.all()
    paginator = Paginator(users,100)
    page = request.GET.get('page')

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page( 1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    index = users.number -1
    max_index = len(paginator.page_range)
    start_index = index -5 if index >= 5 else 0 
    end_index = index + 5 if index <=max_index  -5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            #Q(name__icontains=query)|
            Q(shop_name__icontains=query)
            #Q(description__icontains=query)|
            #Q(created__icontains=query)
        )
        users = User.objects.filter(
            Q(is_shop__icontains=query)
        )
    

    return render (request, 'Profile/shop.html', {'users': users,'friends':friends,  'page_range': page_range })

#end view

#this is the view for the shop admin
@method_decorator([login_required, shop_required], name='dispatch')
class ShopadminView(TemplateView):
    template_name = 'Profile/Shopadmin.html '

    def get(self, request):

        return render(request, self.template_name)

#end shopadmin view


#this is the view for the form that adds products
@method_decorator([login_required, shop_required], name='dispatch')
class ProductFormView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'Profile/product_form.html'
    success_url = reverse_lazy('shopp:product_list')

 
    def form_valid(self, form):
        category = form.cleaned_data.get('category')
        name = form.cleaned_data.get('name')
        slug = form.cleaned_data.get('slug')
        image = form.cleaned_data.get('image')
        image2 = form.cleaned_data.get('image2')
        image3 = form.cleaned_data.get('image3')
        description = form.cleaned_data.get('description')
        price = form.cleaned_data.get('price')
        stock = form.cleaned_data.get('stock')
        
        form.save(self.request.user)
        return super().form_valid(form)


@method_decorator([login_required, shop_required], name='dispatch')    
class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'shopp/product_delete.html'
    success_url = reverse_lazy('shopp:product_list')

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        messages.success(request, 'Your product %s was deleted successfully!!')
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.products.all()



#view that creates a shop        
@method_decorator([login_required, shop_required], name='dispatch')
class ShopFormView(LoginRequiredMixin, CreateView):
    model = Shop
    form_class = ShopForm
    template_name = 'Profile/shopform.html'
    success_url = reverse_lazy('Profile:Profile')

    def form_valid(self, form):
        shop_name = form.cleaned_data.get('shop_name')
        description = form.cleaned_data.get('description')
        city = form.cleaned_data.get('city')
        website = form.cleaned_data.get('website')
        phone = form.cleaned_data.get('phone')
        image = form.cleaned_data.get('image')
        #user = form.save()
        form.save(self.request.user)

        return super().form_valid(form)


class ShopFormUpdate(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = 'Profile/editshop.html'
    success_url = reverse_lazy('Profile:Profile')

    def get_object(self):
        try:
            return self.request.user.shop
        except ObjectDoesNotExist:
            print("hello shop")

    def form_valid(self, form):
        shop_name = form.cleaned_data.get('shop_name')
        description = form.cleaned_data.get('description')
        city = form.cleaned_data.get('city')
        website = form.cleaned_data.get('website')
        phone = form.cleaned_data.get('phone')
        image = form.cleaned_data.get('image')
        form.save(self.request.user)
        return super().form_valid(form)


#view that creates a client userprofile
@method_decorator([login_required, client_required], name='dispatch')
class ClientFormView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'Profile/clientform.html'
    success_url = reverse_lazy( 'login:profile')

#    try:
#        form_class = ClientForm
#    except ObjectDoesNotExist:
#        print("hello")
    def form_valid(self, form):
        
        phone = form.cleaned_data.get('phone')
        city = form.cleaned_data.get('city')
        image = form.cleaned_data.get('image')
        gender = form.cleaned_data.get('gender')
        user = form.save()
        form.save(self.request.user)

        return super().form_valid(form)
 

#start client update view
"""This is the view for clients that helps them in updating their profiles   """ 
@method_decorator([login_required, client_required], name='dispatch')
class ClientFormUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'Profile/editclient.html'
    success_url = reverse_lazy('login:profile')
    
    def get_object(self):
        try:
            return self.request.user.client
        except ObjectDoesNotExist:
            print ( "hello ")
    
    def form_valid(self, form):
        
        phone = form.cleaned_data.get('phone')
        city = form.cleaned_data.get('city')
        image = form.cleaned_data.get('image')
        gender = form.cleaned_data.get('gender')
        user = form.save()
        form.save(self.request.user)
        messages.success(self.request, 'The update was done successfully!!!')

        return super().form_valid(form)

#end client update view

