from django.urls import path

from services import views

app_name = 'services'

urlpatterns = [
    path('', views.CatalogView.as_view(), name='root'),  # ← обрабатывает /catalog/
    path('search/', views.CatalogView.as_view(), name='search'),
    path('<slug:category_slug>/', views.CatalogView.as_view(), name='category'),
    path('<slug:category_slug>/<slug:types_slug>/', views.TypesView.as_view(), name='types'),
]

# urlpatterns = [
#     path('', views.catalog, name='services'),
#     path('search/', views.catalog, name='search'),
#     path('<slug:category_slug>/', views.catalog, name='category'),
#     path('<slug:category_slug>/<slug:types_slug>/', views.types, name='types'),
# ]