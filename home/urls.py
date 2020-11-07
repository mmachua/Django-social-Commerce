from django.conf.urls import url
from django.urls import include, re_path
#from home.views import 
from django.contrib.auth import views as auth_views
from . import views as myapp_views
from home import views
from . import views 
from home.views import ContactView, PrivacyView, TermsView


app_name = 'home'


urlpatterns = [

    re_path(r'^privacy/', PrivacyView.as_view(), name='privacy' ),
    re_path(r'^terms/', TermsView.as_view(), name='terms'),
    
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', 
            views.change_friends, name='change_friends'),
    re_path('contact/', ContactView.as_view(), name='Contact')
  
]


