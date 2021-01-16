from hashlib import md5
from HFhtml.models import Users, Orders
from django.utils.safestring import mark_safe


def get_user_data(email):
    """ Получение данных о пользователе """
    user = Users.objects.filter(email=email).values('email', 'ref', 'vk', 'vk_status', 'inst', 'inst_status', 'phone')
    name = user[0]['email'].split('@')[0]
    ref = user[0]['ref']
    ref_link = md5(str(user[0]['email']).encode()).hexdigest()[-8:]
    vk_status = user[0]['vk_status']
    instagram_status = user[0]['inst_status']
    vk_id = user[0]['vk'] if user[0]['vk'] is not None else ''
    instagram = user[0]['inst'] if user[0]['inst'] is not None else ''
    phone = user[0]['phone'] if user[0]['phone'] is not None else ''
    orders = Orders.objects.filter(email=user[0]['email']).order_by('id')
    sale = mark_safe("<h2 class='dashcard-text-stat'>5%</h2>") \
        if vk_status == 'Подписан' and instagram_status == 'Подписан'\
        else mark_safe("<h2 class='dashcard-text-stat'>0%</h2>")

    return {'name': name, 'ref_link': ref_link, 'ref': ref, 'vk': vk_id, 'vk_status': vk_status,
            'instagram': instagram, 'instagram_status': instagram_status, 'phone': phone, 'sale': sale,
            'orders': orders}


def change_user_data(email, method, data):
    user = Users.objects.get(email=email)
    if method == 'instagram':
        user.inst = data
        Users.check_instagram(user, data)
    if method == 'vk':
        user.vk = data
        Users.check_vk(user, data)
    if method == 'phone':
        user.phone = data
    user.save()
