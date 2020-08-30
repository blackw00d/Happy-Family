from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hashlib import md5
import requests
import json
from HFhtml.models import Users
from django.utils.safestring import mark_safe
from HFhtml.models import OrderItem, Orders


def vk(vk_id):
    url = 'https://api.vk.com/method/groups.getMembers?group_id=174429100&access_token=fc035b21fc035b21fc035b216dfc6b125fffc03fc035b21a04f00868e3eec3221de283a&v=5.92';
    data = json.loads(requests.post(url).text)
    if data['response'] is not None and vk_id is not None:
        for item in data['response']['items']:
            if vk_id == str(item):
                return 'Подписан'
        return 'Не подписан'
    else:
        return 'Не подписан'


@login_required(login_url='Enter')
def lk(request):
    user = Users.objects.filter(email=request.user.email).values('email', 'ref', 'vk', 'inst', 'phone')
    name = user[0]['email'].split('@')[0]
    ref = user[0]['ref']
    ref_link = md5(str(user[0]['email']).encode()).hexdigest()[-8:]
    vk_status = vk(user[0]['vk'])
    instagram_status = user[0]['inst'] if user[0]['inst'] is not None else '-'
    vk_id = user[0]['vk'] if user[0]['vk'] is not None else ''
    instagram = user[0]['inst'] if user[0]['inst'] is not None else ''
    phone = user[0]['phone'] if user[0]['phone'] is not None else ''
    orders = OrderItem.objects.filter(order__email=user[0]['email']).order_by('order_id').all()

    sale = mark_safe(
        " title='Скидка автивируется после проверки Instagram'>5%") if vk_status == 'Подписан' else mark_safe(">0%")
    return render(request, 'HFlk/lk.html',
                  {'name': name, 'ref_link': ref_link, 'ref': ref, 'vk': vk_id, 'vk_status': vk_status,
                   'instagram': instagram, 'instagram_status': instagram_status, 'phone': phone, 'sale': sale,
                   'orders': orders})


def changeinst(request):
    user = Users.objects.get(email=request.user.email)
    user.inst = request.POST['inst']
    user.save()
    return redirect('LK')


def changevk(request):
    user = Users.objects.get(email=request.user.email)
    user.vk = request.POST['vk']
    user.save()
    return redirect('LK')


def changephone(request):
    user = Users.objects.get(email=request.user.email)
    user.phone = request.POST['phone']
    user.save()
    return redirect('LK')
