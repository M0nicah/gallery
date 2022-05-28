from django.conf import settings
from django.urls import URLPattern, re_path
from galleria import views
from django.conf.urls.static import static

urlpatterns = [
    re_path('^$', views.gallery, name='gallery'),
    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)