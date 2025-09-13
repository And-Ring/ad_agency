from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

from ad_agency import settings

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),  # смена языка
]

# i18n_patterns оборачивает маршруты, которые должны учитывать язык
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path("", include("main.urls", namespace='main')),
    path("catalog/", include("services.urls", namespace='catalog')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)