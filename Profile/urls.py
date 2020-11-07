from django.urls import include, re_path
from Profile.views import ProfileView  ,ShopadminView , shop, favouriteshops,AboutView 
from .import views
from .views import ProductFormView , ShopFormView  , ClientFormUpdate ,ClientFormView, ShopFormUpdate

from shopp.views import delete_view
app_name='Profile'

urlpatterns = [
    re_path(r'^$', ProfileView.as_view(), name='Profile'),
    re_path(r'^Profile/(?P<pk>\d+)/$', ProfileView.as_view(), name='view_profile_with_pk'),
    re_path(r'^editclient/$', ClientFormUpdate.as_view(), name='editclient'),
    re_path(r'^Shopadmin/$', ShopadminView.as_view(), name='Shopadmin'),
    re_path(r'^shop/$', views.shop, name='shop'),
    re_path(r'^favouriteshops/$', views.favouriteshops, name='favouriteshops'),
    re_path(r'^about', AboutView.as_view(), name='about'),
    re_path(r'^Profile/(?P<id>\d+)/(?P<slug>[-\w]+)/$', ProfileView.as_view(), name='user_post_detail'),
    re_path('product_form/', ProductFormView.as_view(), name = 'product_form'),
    re_path('shopform/', ShopFormView.as_view(), name='Shopform'),
    re_path('clientform/', ClientFormView.as_view(), name='Clientform'),
    re_path(r'^editshop/$', ShopFormUpdate.as_view(), name = 'editshop' )
    
]

