# from django.http import HttpResponse
# from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from feedback.forms import FeedbackForm


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('RuAd - Главная')
        context['content'] = _('Рекламное агенство "RussianAdvertising"')
        context['text_on_page'] = _(
            'Адрес: г. Москва, ул. Примерная, 10\n'
            'Телефон: +7 (999) 999-99-!!\n'
            'Email: info@ruad!!.ru'
        )
        return context


# def index(request):
#
#
#     context = {
#         'title': _('RuAd - Главная'),
#         'content': _('Рекламное агенство "RussianAdvertising"'),
#         'text_on_page': _(
#             'Адрес: г. Москва, ул. Примерная, 10\n'
#             'Телефон: +7 (999) 999-99-!!\n'
#             'Email: info@ruad!!.ru'
#         ),
#     }
#
#     return render(request, 'main/index.html', context)


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('RuAd - О компании')
        context['content'] = _('О компании')
        context['text_on_page'] = _('Текст о том, почему это агенство такое классное')
        return context



# def about(request):
#     context = {
#         'title': _('RuAd - О компании'),
#         'content': _('О компании'),
#         'text_on_page': _('Текст о том, почему это агенство такое классное'),
#     }
#
#     return render(request, 'main/about.html', context)


class PortfolioView(TemplateView):
    template_name = 'main/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('RuAd - Портфолио')
        context['content'] = _('Портфолио')
        context['text_on_page'] = _('Данная страница находится в разработке!')
        return context


# def portfolio(request):
#     context = {
#         'title': _('RuAd - Портфолио'),
#         'content': _('Портфолио'),
#         'text_on_page': _('Данная страница находится в разработке!'),
#     }
#     return render(request, 'main/portfolio.html', context)


class DeliveryPaymentView(TemplateView):
    template_name = 'main/delivery_payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('RuAd - Доставка и оплата')
        context['content'] = _('Информация о доставке и оплате')
        context['delivery_text'] = _('Мы доставляем по всей России. Сроки зависят от региона. Возможен самовывоз')
        context['payment_text'] = _('Оплата возможна картой, наличными при получении, банковским переводом, через СПБ.')
        return context


# def delivery_payment(request):
#     context = {
#         'title': _('RuAd - Доставка и оплата'),
#         'content': _('Информация о доставке и оплате'),
#         'delivery_text': _('Мы доставляем по всей России. Сроки зависят от региона. Возможен самовывоз'),
#         'payment_text': _('Оплата возможна картой, наличными при получении, банковским переводом, через СПБ.'),
#     }
#     return render(request, 'main/delivery_payment.html', context)


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('RuAd - Контакты')
        context['content'] = _('Контактная информация')
        context['address'] = _('г. Москва, ул. Примерная, 10')
        context['phone'] = _('+7 (999) 999-99-!!')
        context['email'] = _('info@ruad!!.ru')
        context['feedback_form'] = FeedbackForm()
        return context

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        context = self.get_context_data()
        if form.is_valid():
            form.save()
            context['success'] = True
        else:
            context['feedback_form'] = form
        return self.render_to_response(context)


# def contacts(request):
#     context = {
#         'title': _('RuAd - Контакты'),
#         'content': _('Контактная информация'),
#         'address': _('г. Москва, ул. Примерная, 10'),
#         'phone': _('+7 (999) 999-99-!!'),
#         'email': _('info@ruad!!.ru'),
#
#     }
#     return render(request, 'main/contacts.html', context)




