
from django.urls import include, path

from .views import login, client, shop

from django.conf.urls import url
from django.urls import include, re_path
from django.urls import include ,path
from django.contrib.auth.views import (
    login,
    logout,
     password_reset_confirm,
      password_reset,
     password_reset_done,
     password_reset_complete
     )
from django.contrib.auth import views as auth_views
from . import views as myapp_views
from . import views
from  .views import login 

app_name = 'login'

urlpatterns = [

    path('clients/', include(([
        re_path(r'^profile/$',login.ProfileView.as_view(), name='profile'),
        re_path(r'^profile/edit/$', login.edit_profile, name='edit_profile'),
        re_path(r'^change-password/$', login.change_password, name='change_password'),
        re_path(r'^reset-password/$', password_reset,{ 'template_name':
                  'login/reset_password.html','post_reset_redirect':
                  'login:password_reset_done','email_template_name':
                  'login:reset_password_email.html' }, name='reset_password'),
        re_path(r'^reset-password/done/$', password_reset_done, 
                  {'template_name':'login/reset_password_done.html'},
                  name='password_reset_done'),
        re_path(r'^reset-password/confirm/$', password_reset_confirm, name='password_reset_confirm'),

        re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                  password_reset_confirm, {'template_name':
                  'login/reset_password_confirm.html', 'post_reset_redirect':
                  'login:password_reset_complete'},  name='password_reset_confirm'),

        re_path(r'^reset-password/complete/$', password_reset_complete,{'template_name':
                  'login/reset_password_complete.html'}, name='password_reset_complete'),
        re_path(r'^logout/$', logout,{'template_name': 'login/logout.html'}, name='logout'),

        re_path(r'^about/$', login.about, name='about'),
        #re_path(r'^delete/(?P<username>[\w|\W.-]+)/$', views.delete_user, name='delete-user')

    ]))),


    path('shops/', include(([
        #re_path(r'^profile/$',login.ProfileView.as_view(), name='profile'),
        re_path(r'^profile/edit/$', login.edit_profile, name='edit_profile'),
        re_path(r'^change-password/$', login.change_password, name='change_password'),
        
        re_path(r'^reset-password/$',  password_reset,{ 'template_name':
                  'login/reset_password.html','post_reset_redirect':
                  'login:password_reset_done','email_template_name':
                  'login/reset_password_email.html' }, name='reset_password'),
        re_path(r'^reset-password/done/$', password_reset_done, 
                  {'template_name':'login/reset_password_done.html'},
                  name='password_reset_done'),
        re_path(r'^reset-password/confirm/$', password_reset_confirm, name='password_reset_confirm'),
  
        re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                  password_reset_confirm, {'template_name':
                  'login/reset_password_confirm.html', 'post_reset_redirect':
                  'login:password_reset_complete'},  name='password_reset_confirm'),

        re_path(r'^reset-password/complete/$', password_reset_complete,{'template_name':
                  'login/reset_password_complete.html'}, name='password_reset_complete'),
        re_path(r'^logout/$', logout,{'template_name': 'login/logout.html'}, name='logout'),

        re_path(r'^about/$', login.about, name='about')

    ])))
 
]





    