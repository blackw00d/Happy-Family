from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_todo_items, name='Index'),
    path('AddCall/', views.AddCall.as_view(), name='AddCall'),
    path('BasketAdd/', views.basketadd, name='BasketAdd'),
    path('BasketRemove/', views.basketremove, name='BasketRemove'),
    path('Checkout/', views.checkout, name='Checkout'),
    path('MakeOrder/', views.makeorder, name='MakeOrder')
]
