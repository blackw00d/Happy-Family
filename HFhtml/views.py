from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import CallForm
from .services import *


class AddCall(View):
    """ Форма обратной связи, добавление информации о пользователе в базу данных,
        отправка сообщения в группу Telegram """

    def post(self, request):
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
            telegram_add_call(request.POST.get('phone', None))
        return redirect('/')


def basket_add(request):
    """ Добавление товара в корзину """
    name = request.POST.get('name', None)
    price = request.POST.get('price', None)

    image_url = get_item_image(name)
    data = add_item_to_basket(request.session['basket'], name, price, image_url)
    request.session.modified = True

    return HttpResponse(data)


def basket_remove(request):
    """ Удаление товара из корзины """
    name = request.POST.get('name', None)
    basket = request.session['basket']
    basket.pop(name)
    request.session.modified = True
    return HttpResponse('')


def make_order(request):
    """ Создание заказа """
    if 'basket' not in request.session:
        return redirect('../')
    if 'city' not in request.session:
        return redirect('../')

    basket = request.session['basket']
    phone = request.POST.get('phone', None)
    email = request.POST.get('email', None)
    pay = request.POST.get('selector', None)
    city = request.session['city']
    if not phone or not email or not pay or basket == {}:
        return redirect('../')

    created = create_order(phone, email, pay, city)
    if created and email:
        send_email(email, created, pay)
    telegram_make_order(phone, created, city)
    add_items_to_order(basket, created, city)
    request.session.modified = True

    return render(request, 'HFhtml/checkout.html', {'success': True, 'order': created})


def checkout(request):
    """ Оформление заказа в отдельном окне """
    if 'basket' not in request.session:
        return index(request)

    return render(request, 'HFhtml/checkout.html',
                  get_basket_with_len(request.session['basket'], request.session['city']))


def change_city(request):
    """ Смена города """
    city = request.POST.get('city', 'Сургут')
    request.session['city'] = city
    request.session['basket'] = {}

    return redirect('/')


def index(request):
    """ Главная страница сайта """
    if 'basket' not in request.session:
        request.session['basket'] = {}
    if 'city' not in request.session:
        request.session['city'] = 'Сургут'

    itemlist = get_all_items(request.session['city'])
    cities = get_all_cities()
    context = {'items': itemlist, 'cities': cities, 'city': request.session['city']}
    context.update(get_basket_with_len(request.session['basket'], request.session['city']))

    return render(request, 'HFhtml/index.html', context)
