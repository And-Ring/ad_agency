from django.db import models
from django.utils.translation import gettext_lazy as _


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_('Название'))
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name=_('URL'))
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'category'
        verbose_name = _('Категорию')
        verbose_name_plural = _('Категории')
        ordering = ['order']  # или ['order', 'name']


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if hasattr(self, 'name_en') and self.name_en:
            self.slug = self.name_en.lower().replace(' ', '-')
        super().save(*args, **kwargs)


class Types(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_('Название'))
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name=_('URL'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    image_path = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Изображение'))
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name=_('Категория'))


    class Meta:
        db_table = 'type'
        verbose_name = _('Вид')
        verbose_name_plural = _('Виды')
        ordering = ('id',)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if hasattr(self, 'name_en') and self.name_en:
            self.slug = self.name_en.lower().replace(' ', '-')
        super().save(*args, **kwargs)

