from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .services import *


def index(request):
    """ Главная страница """
    if request.user.is_authenticated:
        return redirect('LK')
    ref = request.GET.get('ref', None)
    forget = request.GET.get('forget', None)
    if ref is not None:
        if len(ref) != 8:
            ref = None
    if forget is not None:
        if len(forget) != 32:
            forget = None

    return render(request, 'HFadmin/admin.html', {'ref': ref, 'new': forget})


def logout_view(request):
    """ Закрытие сессии пользователя при выходе из ЛК с сохранением корзины """
    for key in list(request.session.keys()):
        if key != 'basket':
            del request.session[key]
    return redirect('../../')


def signin(request):
    """ Авторизация """
    if request.user.is_authenticated:
        return redirect('../../lk')

    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    if email is None or password is None:
        signup_err = get_error('Введите email и пароль')
        return render(request, 'HFadmin/admin.html', {'signup_err': signup_err})

    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('../../lk')
    else:
        auth_err = get_error('Неправильный email или пароль')
        return render(request, 'HFadmin/admin.html', {'auth_err': auth_err})


def signup(request):
    """ Регистрация """
    if request.user.is_authenticated:
        return redirect('../../lk')

    email = request.POST.get('email', None)
    password = request.POST.get('pass1', None)
    ref = request.POST.get('ref_id', None)
    if email is None or password is None:
        signup_err = get_error('Введите email и пароль')
        return render(request, 'HFadmin/admin.html', {'signup_err': signup_err, 'ref': 'Referal (Option)'})

    created = create_user(email, password)
    if created is not None:
        user = authenticate(request, username=email, password=password)
        if ref is not None:
            update_ref_counter(ref)
        if user is not None:
            login(request, user)
            send_email('', email, 'signup')
        return redirect('../../lk')
    else:
        signup_err = get_error('Такой пользователь уже существует')
        return render(request, 'HFadmin/admin.html', {'signup_err': signup_err, 'ref': ref})


def reset_pass(request):
    """ Форма восстановление пароля """
    if request.user.is_authenticated:
        return redirect('../../lk')

    reset_err = get_error('Неправильный email')
    if request.POST:
        email = request.POST.get('email', None)
        if email is None:
            return render(request, 'HFadmin/admin.html', {'reset_err': reset_err})
        reset_err = send_reset_pass(email)
        return render(request, 'HFadmin/admin.html', {'reset_err': reset_err})
    else:
        return render(request, 'HFadmin/admin.html', {'reset_err': reset_err})


def new_pass(request):
    """ Форма установка нового пароля """
    if request.user.is_authenticated:
        return redirect('../../lk')

    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    password_confirmation = request.POST.get('password_confirmation', None)
    forget = request.POST.get('forget', None)

    if email is None or password is None or forget is None:
        new_err = get_error('Введите email и пароль')
        return render(request, 'HFadmin/admin.html', {'new_err': new_err, 'new': True})

    if password != password_confirmation:
        new_err = get_error('Пароли не совпадают')
        return render(request, 'HFadmin/admin.html', {'new_err': new_err, 'new': True})

    response = set_new_pass(email, password, forget)
    return render(request, 'HFadmin/admin.html', response)
