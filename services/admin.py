from django.contrib import admin
from .models import Categories, Types


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')   # поля в списке
    search_fields = ('name', 'slug')        # поиск
    prepopulated_fields = {'slug': ('name_en',)}


@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')  # покажем категорию
    search_fields = ('name', 'description')   # поиск
    list_filter = ('category',)               # фильтр по категориям
    prepopulated_fields = {'slug': ('name',)}
    fields = ['name', 'slug', 'description', 'image_path', 'category']