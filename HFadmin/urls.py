from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Enter'),
    path('logout/', views.logout_view, name='LogOut'),
    path('signin/', views.signin, name='SignIn'),
    path('signup/', views.signup, name='SignUp'),
    path('reset/', views.reset_pass, name='Reset'),
    path('newpass/', views.new_pass, name='NewPass')
]
