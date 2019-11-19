from django.urls import path, re_path
from .views import vendor_create, vendor_list, delete_view, address_view

app_name = 'vendor'

urlpatterns = [
    path('', vendor_create, name='vendor'),
    path('list/', vendor_list, name='vendor_list'),
    re_path(r'^address/(?P<id>\d+)/$', address_view, name='vendor_address'),
    re_path(r'^delete/(?P<id>\d+)/$', delete_view, name='delete'),
]
