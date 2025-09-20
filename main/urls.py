from django.urls import path
from django.views.decorators.cache import cache_page
from main import views


app_name = 'main'

urlpatterns = [
    # Главная страница — без полного кэша, чтобы всегда был актуальный контент
    path('', views.IndexView.as_view(), name='index'),

    # Статичные страницы — кэшируем на сутки
    path('about/', cache_page(60 * 60 * 24)(views.AboutView.as_view()), name='about'),
    path('portfolio/', cache_page(60 * 60 * 24)(views.PortfolioView.as_view()), name='portfolio'),
    path('delivery-payment/', cache_page(60 * 60 * 24)(views.DeliveryPaymentView.as_view()), name='delivery_payment'),
    path('contacts/', cache_page(60 * 60 * 24)(views.ContactsView.as_view()), name='contacts'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('portfolio/', views.portfolio, name='portfolio'),
#     path('delivery-payment/', views.delivery_payment, name='delivery_payment'),
#     path('contacts/', views.contacts, name='contacts'),
#
# ]