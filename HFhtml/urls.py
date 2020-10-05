from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),
    path('AddCall/', views.AddCall.as_view(), name='AddCall'),
    path('BasketAdd/', views.basket_add, name='BasketAdd'),
    path('BasketRemove/', views.basket_remove, name='BasketRemove'),
    path('Checkout/', views.checkout, name='Checkout'),
    path('MakeOrder/', views.make_order, name='MakeOrder')
]
