from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils.translation import gettext as _

from services.models import Types, Categories
from services.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)

    if category_slug == 'all-services':
        services = Types.objects.all()
    elif query:
        services = q_search(query)
    else:
        services = get_list_or_404(Types.objects.filter(category__slug=category_slug))

    paginator = Paginator(services, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': _('RuAd - Услуги'),
        'services': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'services/catalog.html', context)


def types(request, category_slug, types_slug):

    types = get_object_or_404(Types, slug=types_slug, category__slug=category_slug)

    context = {
        'types': types,
    }

    return render(request, 'services/types.html', context=context)
