from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from services.models import Categories, Types


register = template.Library()


def get_name_by_slug(slug):
    """Пробует найти читаемое имя по slug: сначала по фиксированным, потом в БД."""

    static_titles = {
        'catalog': _('Услуги'),
        'about': _('О компании'),
        'contacts': _('Контакты'),
        'delivery-payment': _('Доставка и оплата'),
        'portfolio': _('Портфолио'),
        'feedback': _('Обратная связь'),
        
    }

    if slug in static_titles:
        return static_titles[slug]

    for model in [Categories, Types]:
        obj = model.objects.filter(slug=slug).first()
        if obj:
            return obj.name

    return None


@register.simple_tag(takes_context=True)
def breadcrumbs(context):
    request = context['request']
    path = request.path.strip('/')

    if not path:
        return ''  # Главная страница

    parts = path.split('/')
    crumbs = []
    url = ''

    for i, part in enumerate(parts):
        name = get_name_by_slug(part)
        if name is None:
            continue  # Пропускаем, например, 'all'

        url += f'/{part}'

        if i < len(parts) - 1:
            crumbs.append(f'<a href="{url}/" class="link-secondary text-decoration-none">{name}</a>')
        else:
            crumbs.append(f'<span class="text-secondary">{name}</span>')

    full_html = f'<a href="/" class="link-secondary text-decoration-none">{_("Главная")}</a> &raquo; ' + ' &raquo; '.join(crumbs)
    return mark_safe(full_html)