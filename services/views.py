# from django.core.paginator import Paginator
# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.cache import cache
from django.http import Http404
from django.views.generic import DetailView, ListView
from django.utils.translation import gettext as _, get_language

from services.models import Types, Categories
from services.utils import q_search


class CatalogView(ListView):
    model = Types
    # queryset = Types.objects.all().order_by('-id')
    template_name = 'services/catalog.html'
    context_object_name = 'services'
    paginate_by = 3
    allow_empty = True

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        query = self.request.GET.get('q')

        if query:
            return q_search(query)

        if category_slug == 'all-services' or category_slug is None:
            return super().get_queryset()  # ← покажет все услуги и по маршруту /catalog/

        if category_slug:
            services = super().get_queryset().filter(category__slug=category_slug)
            if services.exists():
                return services

        return super().get_queryset().none()  # безопасный fallback — ничего не найдено

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('RuAd - Услуги')
        context['slug_url'] = self.kwargs.get('category_slug')
        # context['categories'] = Categories.objects.all()

        # --- Кэшируем категории с учётом языка ---
        lang = get_language()
        cache_key = f'categories_list_{lang}'
        categories = cache.get(cache_key)
        if not categories:
            categories = list(Categories.objects.all())
            cache.set(cache_key, categories, 3600)  # 1 час
        context['categories'] = categories

        return context


class TypesView(DetailView):

    # model = Types
    # queryset = Types.objects.all()
    # slug_field = 'slug'
    template_name = 'services/types.html'
    slug_url_kwarg = 'types_slug'
    context_object_name = 'types'

    def get_object(self, queryset=None):
        services = Types.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return services

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name

        lang = get_language()
        cache_key = f'categories_list_{lang}'
        categories = cache.get(cache_key)
        if not categories:
            categories = list(Categories.objects.all())
            cache.set(cache_key, categories, 3600)
        context['categories'] = categories

        return context


# def catalog(request, category_slug=None):
#
#     page = request.GET.get('page', 1)
#     query = request.GET.get('q', None)
#
#     if category_slug == 'all-services':
#         services = Types.objects.all()
#     elif query:
#         services = q_search(query)
#     else:
#         services = get_list_or_404(Types.objects.filter(category__slug=category_slug))
#
#     paginator = Paginator(services, 3)
#     current_page = paginator.page(int(page))
#
#     context = {
#         'title': _('RuAd - Услуги'),
#         'services': current_page,
#         'slug_url': category_slug,
#     }
#     return render(request, 'services/catalog.html', context)
#
#
# def types(request, category_slug, types_slug):
#
#     types = get_object_or_404(Types, slug=types_slug, category__slug=category_slug)
#
#     context = {
#         'types': types,
#     }
#
#     return render(request, 'services/types.html', context=context)
