from modeltranslation.translator import translator, TranslationOptions
from .models import Categories, Types


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # у категорий переводим только название


class TypeTranslationOptions(TranslationOptions):
    fields = ('name', 'description')  # у видов услуг переводим и название, и описание


translator.register(Categories, CategoryTranslationOptions)
translator.register(Types, TypeTranslationOptions)