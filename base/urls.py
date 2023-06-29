from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from base.views import *
handler404 = pageNotFound
urlpatterns = [
    path('', mainpage,name="base"),
    path("birthday/<slug:birthid>/",categories,name="birthday"),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive,name="archive")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)