from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hashlib import md5
import requests
import json
from HFhtml.models import Users
from django.utils.safestring import mark_safe
from HFhtml.models import OrderItem


def _vk(vk_id):
    """ Проверка подписки на группу в ВК """
    url = "https://api.vk.com/method/groups.getMembers?group_id=174429100&access_token" \
          "=fc035b21fc035b21fc035b216dfc6b125fffc03fc035b21a04f00868e3eec3221de283a&v=5.92 "
    data = json.loads(requests.post(url).text)
    if data['response'] is not None and vk_id is not None:
        for item in data['response']['items']:
            if vk_id == str(item):
                return 'Подписан'
        return 'Не подписан'
    else:
        return 'Не подписан'


def _get_user_stats(email):
    """ Получение данных о пользователе """
    user = Users.objects.filter(email=email).values('email', 'ref', 'vk', 'inst', 'phone')
    name = user[0]['email'].split('@')[0]
    ref = user[0]['ref']
    ref_link = md5(str(user[0]['email']).encode()).hexdigest()[-8:]
    vk_status = _vk(user[0]['vk'])
    instagram_status = user[0]['inst'] if user[0]['inst'] is not None else '-'
    vk_id = user[0]['vk'] if user[0]['vk'] is not None else ''
    instagram = user[0]['inst'] if user[0]['inst'] is not None else ''
    phone = user[0]['phone'] if user[0]['phone'] is not None else ''
    orders = OrderItem.objects.filter(order__email=user[0]['email']).order_by('order_id').all()
    sale = mark_safe(
        " title='Скидка автивируется после проверки Instagram'>5%") if vk_status == 'Подписан' else mark_safe(">0%")

    return {'name': name, 'ref_link': ref_link, 'ref': ref, 'vk': vk_id, 'vk_status': vk_status,
            'instagram': instagram, 'instagram_status': instagram_status, 'phone': phone, 'sale': sale,
            'orders': orders}


def _change_user_data(email, method, data):
    user = Users.objects.get(email=email)
    if method == 'instagram':
        user.inst = data
    if method == 'vk':
        user.vk = data
    if method == 'phone':
        user.phone = data
    user.save()


@login_required(login_url='Enter')
def lk(request):
    user_stats = _get_user_stats(request.user.email)
    return render(request, 'HFlk/lk.html', user_stats)


def change_instagram(request):
    _change_user_data(request.user.email, 'instagram', request.POST['inst'])
    return redirect('LK')


def change_vk(request):
    _change_user_data(request.user.email, 'vk', request.POST['vk'])
    return redirect('LK')


def change_phone(request):
    _change_user_data(request.user.email, 'phone', request.POST['phone'])
    return redirect('LK')
