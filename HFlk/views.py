from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .services import *


@login_required(login_url='Enter')
def lk(request):
    user_stats = get_user_data(request.user.email)
    return render(request, 'HFlk/lk.html', user_stats)


def change_instagram(request):
    change_user_data(request.user.email, 'instagram', request.POST['inst'])
    return redirect('LK')


def change_vk(request):
    change_user_data(request.user.email, 'vk', request.POST['vk'])
    return redirect('LK')


def change_phone(request):
    change_user_data(request.user.email, 'phone', request.POST['phone'])
    return redirect('LK')
