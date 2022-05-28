from django.urls import URLPattern, re_path
from galleria import views

urlpatterns = [
    re_path('^$', views.welcome, name='welcome'),
    ]