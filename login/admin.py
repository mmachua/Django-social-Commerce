from django.contrib import admin
from login.models import Shop, Client, User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ( 'username', 'first_name', 'last_name' ,'email','is_client', 'is_shop')

    def user_info(self, obj):
        return obj.description

def get_queryset(self, request):
    queryset = super(UserAdmin, self).get_queryset(request)
    queryset = queryset.order_by('username', 'first_name')
    return queryset
    

admin.site.register(User, UserAdmin)


class ShopAdmin(admin.ModelAdmin):
    list_display = ('user', 'shop_name', 'user_info','city', 'phone', 'description')

    def user_info(self, obj):
        return obj.description

admin.site.register(Shop, ShopAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('user','gender' ,'image', 'city', 'phone')

    def user_info(self, obj):
        return obj.description

admin.site.register(Client, ClientAdmin)



