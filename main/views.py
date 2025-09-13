from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

from services.models import Categories


def index(request):


    context = {
        'title': _('RuAd - Главная'),
        'content': _('Рекламное агенство "RussianAdvertising"'),
        'text_on_page': _(
            'Адрес: г. Москва, ул. Примерная, 10\n'
            'Телефон: +7 (999) 999-99-!!\n'
            'Email: info@ruad!!.ru'
        ),
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': _('RuAd - О компании'),
        'content': _('О компании'),
        'text_on_page': _('Текст о том, почему этот магазин такой классный'),
    }

    return render(request, 'main/about.html', context)


def portfolio(request):
    context = {
        'title': _('RuAd - Портфолио'),
        'content': _('Портфолио'),
        'text_on_page': _('Данная страница находится в разработке!'),
    }
    return render(request, 'main/portfolio.html', context)


def delivery_payment(request):
    context = {
        'title': _('RuAd - Доставка и оплата'),
        'content': _('Информация о доставке и оплате'),
        'delivery_text': _('Мы доставляем по всей России. Сроки зависят от региона. Возможен самовывоз'),
        'payment_text': _('Оплата возможна картой, наличными при получении, банковским переводом, через СПБ.'),
    }
    return render(request, 'main/delivery_payment.html', context)


def contacts(request):
    context = {
        'title': _('RuAd - Контакты'),
        'content': _('Контактная информация'),
        'address': _('г. Москва, ул. Примерная, 10'),
        'phone': _('+7 (999) 999-99-!!'),
        'email': _('info@ruad!!.ru'),

    }
    return render(request, 'main/contacts.html', context)




