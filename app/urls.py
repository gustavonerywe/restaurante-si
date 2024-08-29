from django.urls import path
from .views import * 

urlpatterns = [
    path('', index, name='index'),
    path('customer/', customer, name='customer'),
    path('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('edit_customer/<int:customer_id>/', edit_customer, name='edit_customer'),
    path('menu/', menu, name='menu'),
    path('category/', category, name='category'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),
    path('edit_category/<int:category_id>/', edit_category, name='edit_category'),
    path('item/', items, name='items'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('edit_item/<int:item_id>/', edit_item, name='edit_item'),
]