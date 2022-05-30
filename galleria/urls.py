from django.conf import settings
from django.urls import URLPattern, re_path,path
from galleria import views
from django.conf.urls.static import static

urlpatterns = [
    re_path('^$', views.gallery, name='gallery'),
    path('add_image/',views.add_image, name='add_image'),
    path('update_image/<str:pk>',views.update_image, name='update_image'),
    path('delete_image/<str:pk>',views.delete_image, name='delete_image'),
    path('search_image/', views.search_image, name="search_image"),

    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)