from django.urls import path

from main import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('delivery-payment/', views.delivery_payment, name='delivery_payment'),
    path('contacts/', views.contacts, name='contacts'),

]