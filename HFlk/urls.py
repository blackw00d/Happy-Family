from django.urls import path
from . import views

urlpatterns = [
    path('', views.lk, name='LK'),
    path('changeinst/', views.changeinst, name='ChangeInst'),
    path('changevk/', views.changevk, name='ChangeVk'),
    path('changephone/', views.changephone, name='ChangePhone')
]
