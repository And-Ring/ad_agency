from django.urls import path

from services import views

app_name = 'services'

urlpatterns = [
    path('', views.catalog, name='services'),
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='category'),
    path('<slug:category_slug>/<slug:types_slug>/', views.types, name='types'),
]