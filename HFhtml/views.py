from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.views.generic.base import View
from HappyFamily.settings import EMAIL_HOST_USER
from .models import Items, Images, Orders, OrderItem, Users
from .forms import CallForm
from django.core.mail import send_mail


def send_email(email, created, pay_method):
    if pay_method == 'online':
        pay = "Для оплаты нажмите на кнопку " \
                    "</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "height =\"25\" align=\"left\" valign=\"top\"></td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" height=\"50\">" \
                    "<table " \
                    "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" width=\"126\"></td>" \
                    "<td " \
                    "align =\"center\" valign=\"middle\" height=\"50\" width=\"248\" bgcolor=\"#0082b2\" " \
                    "style=\"font-size:14px;line-height:19px;color:#ffffff;font-family:Arial, Helvetica, " \
                    f"sans-serif;\"><a href=\"https://hf86.ru/enter/?forget={email}\" target=\"_blank\" " \
                    "style=\"color:#ffffff;text-decoration:none;\"><span " \
                    "style=\"font-size:14px;line-height:19px;color:#ffffff;font-family:Arial, Helvetica, " \
                    "sans-serif;\">Оплатить</span></a></td>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" width=\"126\"></td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "height =\"25\" align=\"left\" valign=\"top\"></td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font-family" \
                    ":Arial, Helvetica, sans-serif;\">Или скопируйте данную строку в браузер:<br>" \
                    "<a " \
                    f"href =\"https://hf86.ru/enter/?forget={email}\" target=\"_blank\" " \
                    "style=\"text-decoration: none;color:#0082b2;\"><span " \
                    f"style=\"color:#0082b2;\">https://hf86.ru/enter/?forget={email}</span></a>" \
                    "</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "height =\"30\" align=\"left\" valign=\"top\"></td>" \
                    "</tr>"
    else:
        pay = "Наш менеджер свяжется с Вами в ближайшее время.<br><br>Для отслеживания заказа зарегистрируйтесь на сайте.<br>" \
                    "</td>" \
                    "</tr>"
    message = "<!DOCTYPE " \
                    "html>" \
                    "<html " \
                    "lang=\"en\">" \
                    "<head>" \
                    "<link rel=\"icon\" href=\"https://hf86.ru/img/logo.ico\">" \
                    "<meta charset=\"UTF-8\">" \
                    "<title>Happy " \
                    "Family " \
                    "Surgut </title>" \
                    "<link rel =\"stylesheet\" href=\"https://use.fontawesome.com/releases/v5.3.1/css/all.css\" " \
                    "integrity=\"sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU\" " \
                    "crossorigin=\"anonymous\">" \
                    "</head>" \
                    "<body>" \
                    "<table " \
                    "width =\"100%ds\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"center\" valign=\"top\">" \
                    "<table " \
                    "width =\"640\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" width=\"600\">" \
                    "<table " \
                    "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" height=\"15\"></td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\">" \
                    "<table " \
                    "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" width=\"95\" height=\"36\"><a href=\"https://hf86.ru\" " \
                    "target=\"_blank\"><img src=\"https://hf86.ru/img/logo.png\" width=\"95\" " \
                    "style=\"display:block;\" " \
                    "border=\"0\" alt=\"Happy Family\"></a>" \
                    "</td>" \
                    "<td " \
                    "align =\"right\" valign=\"middle\" style=\"font-family:Arial, Helvetica, " \
                    "sans-serif;font-size:12px;line-height:15px;color:#585858;\">" \
                    "HAPPY FAMILY SURGUT" \
                    "</td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" height=\"25\">" \
                    "</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" style=\"border:1px solid #dddddd;\" bgcolor=\"#ffffff\">" \
                    "<table " \
                    "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" width=\"49\">" \
                    "</td>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" width=\"500\">" \
                    "<table " \
                    "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" height=\"50\"></td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    " align =\"left\" valign=\"top\" style=\"font-size:22px;line-height:28px;color:#333333;font-weight" \
                    f":bold;font-family:Arial, Helvetica, sans-serif;\">Здравствуйте,</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "height =\"20\" align=\"left\" valign=\"top\"></td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font-family" \
                    ":Arial, Helvetica, sans-serif;\">" \
                    f"Вы сделали <strong>{created}</strong> на сайте " \
                    "<a href =\"https://hf86.ru\" target=\"_blank\" style=\"text-decoration:none;color:#585858;\"><span " \
                    "style=\"text-decoration:none;color:#585858;\">hf86.ru</span></a>." \
                    "<br><br>" \
                    f"{pay}" \
                    "<tr>" \
                    "<td " \
                    "height =\"30\" align=\"left\" valign=\"top\" style=\"border-top:1px solid #dddddd;\"></td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font-family" \
                    ":Arial, Helvetica, sans-serif;\">Спасибо, что Вы выбрали <a href=\"https://hf86.ru\" " \
                    "target=\"_blank\" style=\"text-decoration:none;color:#585858;\"><span " \
                    "style=\"text-decoration:none;color:#585858;\">hf86.ru</span></a>. Удачи!<br><br>" \
                    "<strong> С уважением, команда Happy Family </strong>" \
                    "</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td align =\"left\" valign=\"top\" height=\"50\"></td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "</td>" \
                    "<td align =\"left\" valign=\"top\" width=\"49\"></td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td align =\"left\" valign=\"top\" height=\"40\"></td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "</td>" \
                    "<td align =\"center\" valign=\"top\" width=\"20\"></td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "<table width =\"640\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" width=\"20\"></td>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" width=\"600\">" \
                    "<table " \
                    "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"center\" valign=\"top\"><a href=\"https://hf86.ru\" target=\"_blank\"><img " \
                    "src=\"https://hf86.ru/img/logo.png\" width=\"95\" border=\"0\" alt=\"Logo\"></a></td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font-family:Arial, Helvetica, sans-serif;\">" \
                    "Happy Family Surgut " \
                    "</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" height=\"20\"></td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"center\" valign=\"top\">" \
                    "<table " \
                    "<table " \
                    "width =\"100%\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\">" \
                    "<tbody>" \
                    "<tr>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" width=\"120\"></td>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" width=\"30\">" \
                    "<a" \
                    "href =\"https://instagram.com/happyfamily_hmao\" title=\"Instagram\" style=\"color:blue\">" \
                    "<img " \
                    "src =\"https://hf86.ru/img/icons/instagram.png\" height=\"20\">" \
                    "</a>" \
                    "</td>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" width=\"30\">" \
                    "<a " \
                    "href =\"https://vk.com/happyfamily_hmao\" title=\"VK\" style=\"color:blue\">" \
                    "<img " \
                    "src =\"https://hf86.ru/img/icons/vk.png\" height=\"20\">" \
                    "</a>" \
                    "</td>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" width=\"120\"></td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "</td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"left\" valign=\"top\" height=\"30\"></td>" \
                    "</tr>" \
                    "<tr>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" style=\"font-size:11px;line-height:16px;color:#585858;font-family:Arial, Helvetica, sans-serif;\">" \
                    "Copyright © 2020" \
                    "</td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "</td>" \
                    "<td " \
                    "align =\"center\" valign=\"top\" width=\"20\"></td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "</td>" \
                    "</tr>" \
                    "</tbody>" \
                    "</table>" \
                    "</body>" \
                    "</html>"
    subject_text = f"{created} на сайте Happy Family"

    send_mail(subject=subject_text, from_email=EMAIL_HOST_USER, recipient_list=[email],
              html_message=message, message=message)
    return True


class AddCall(View):
    def post(self, request):
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('/')


def basketadd(request):
    name = request.POST.get('name', None)
    price = request.POST.get('price', None)
    item = Items.objects.filter(name=name).values('id')[0]['id']
    imgurl = Images.objects.filter(name_id=item).values('image').first()['image']

    basket = request.session['basket']
    append = basket.get(name, None)
    basket.update({name: {'price': price, 'img': imgurl}})
    request.session.modified = True

    if not append:
        data = mark_safe(f"<div class=\"product\"><div class=\"product-image\"><img src=\"media/{imgurl}\"></div><div "
                         f"class=\"product-details\"><div class=\"product-title\">{name}</div></div><div "
                         f"class=\"product-price\">{price} &#x20BD;</div><div class=\"product-removal\"><a "
                         f"href=\"#\" class=\"remove-product\" data-name=\"{name}\"><i class=\"fas "
                         "fa-trash-alt\"></i></a></div></div>")
    else:
        data = ''

    return HttpResponse(data)


def basketremove(request):
    name = request.POST.get('name', None)
    basket = request.session['basket']
    basket.pop(name)
    request.session.modified = True

    return HttpResponse('')


def makeorder(request):
    if not request.session.has_key('basket'):
        return redirect('../')

    basket = request.session['basket']
    phone = request.POST.get('phone', None)
    email = request.POST.get('email', None)
    pay = request.POST.get('selector', None)
    if not phone or not email or not pay or basket == {}:
        return redirect('../')

    created = Orders.objects.create(phone=phone, email=email, pay=pay)
    if created and email:
        send_email(email, created, pay)

    for item in basket:
        item_name = Items.objects.get(name=item)
        OrderItem.objects.create(order=created, item=item_name)

    basket.clear()
    request.session.modified = True

    return render(request, 'HFhtml/checkout.html', {'success': True, 'order': created})


def checkout(request):
    if not request.session.has_key('basket'):
        return list_todo_items(request)

    basket = request.session['basket']
    basket_len = len(basket.values())
    return render(request, 'HFhtml/checkout.html', {'basket': basket, 'basket_len': basket_len})


def list_todo_items(request):
    itemlist = Items.objects.all().order_by('id')

    # Создание сессии
    if not request.session.has_key('basket'):
        request.session['basket'] = {}
    basket = request.session['basket']
    basket_len = len(basket.values())

    return render(request, 'HFhtml/index.html', {'items': itemlist, 'basket': basket, 'basket_len': basket_len})
