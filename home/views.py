
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
#from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from login.models import User
#from home.forms import HomeForm, HomeCreate
#from home.models import Post, Friend
#from .models import Create
from home.forms import ContactForm
from home.models import Contact, Privacy, Terms
from login.models import Client, Shop
from .models import Friend
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy
from random import randint


@login_required
def home(request):
    return render(request, 'core/home.html')


@login_required
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
        return redirect('Profile:shop')
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('Profile:favouriteshops') 



class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('shopp:product_list')

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
           # title = 'Thanks!!'
            #confirm_message = 'Thanks for messages. we will get right back to you!'
        
        return redirect('shopp:product_list')



class PrivacyView(TemplateView):
    template_name = 'home/privacy.html'

    def get(self, request):
        #form = PrivacyForm()
        privacy = Privacy.objects.all()#.order_by('-date')

        args = {'privacy': privacy }
        return render(request, self.template_name, args)

    def post(self, request):
        form = PrivacyForm()
        if form.is_valid():
            #privacy = form.save(commit=False)
            privacy = get_object_or_404(Privacy, id=id, slug=slug)
            privacy.user = request.user
            privacy.save()
            return redirect('home:privacy')
        args = {'privacy':privacy }
        return render(request, self.template_name, args)   


class TermsView(TemplateView):
    template_name = 'home/terms.html'

    def get(self, request):
        terms = Terms.objects.all()
        args = {'terms':terms }
        return render(request, self.template_name, args)

    def post(self, request):
        if form.is_valid():
            terms = get_object_or_404(Terms)
            terms.user = request.user
            terms.user()
            return redirect('home:terms')

        args = {'terms':terms}
        return render(request, self.template_name, args)