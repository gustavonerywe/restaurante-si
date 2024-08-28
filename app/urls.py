from django.urls import path
from .views import * 

urlpatterns = [
    path('', index, name='index'),
    path('customer/', customer, name='customer'),
    path('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('edit_customer/<int:customer_id>/', edit_customer, name='edit_customer'),
    path('menu/', menu, name='menu'),
    path('REMOVIDO/', REMOVIDO, name='REMOVIDO'),
    path('delete_REMOVIDO/<int:REMOVIDO_id>/', delete_REMOVIDO, name='delete_REMOVIDO'),
    path('edit_REMOVIDO/<int:REMOVIDO_id>/', edit_REMOVIDO, name='edit_REMOVIDO'),
]