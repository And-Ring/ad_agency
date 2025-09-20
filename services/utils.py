from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.utils.translation import get_language
from django.db.models import Q

from services.models import Types


def q_search(query):
    lang = get_language()
    pg_config = {
        'ru': 'russian',
        'en': 'english',
        'de': 'german',
    }.get(lang, 'simple')  # fallback на 'simple' если язык не поддерживается

    # Поиск по ID, если введено число
    if query.isdigit() and len(query) <= 5:
        return Types.objects.filter(id=int(query))

    field_name = f'name_{lang}'
    desc_field = f'description_{lang}'

    # Полнотекстовый поиск
    vector = SearchVector(field_name, desc_field, config=pg_config)
    search_query = SearchQuery(query, config=pg_config)

    result = (
        Types.objects.annotate(rank=SearchRank(vector, search_query))
        .filter(rank__gt=0)
        .order_by("-rank")
        .annotate(
            headline=SearchHeadline(
                field_name,
                search_query,
                start_sel='<mark>',
                stop_sel='</mark>',
                config=pg_config,
            ),
            bodyline=SearchHeadline(
                desc_field,
                search_query,
                start_sel='<mark>',
                stop_sel='</mark>',
                config=pg_config,
            )
        )
    )

    return result

    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_objects = Q()
    #
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #
    # return Types.objects.filter(q_objects)