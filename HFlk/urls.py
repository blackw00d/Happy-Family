from django.urls import path
from . import views

urlpatterns = [
    path('', views.lk, name='LK'),
    path('changeinst/', views.change_instagram, name='ChangeInstagram'),
    path('changevk/', views.change_vk, name='ChangeVk'),
    path('changephone/', views.change_phone, name='ChangePhone')
]
