from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path

from djangoProject import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path(_("admin/"), admin.site.urls),
    path("", include('apps.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    re_path(r'^rosetta/', include('rosetta.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)