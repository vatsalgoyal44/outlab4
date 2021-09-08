from django.conf.urls import url 
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^signup/$', views.register, name = 'register'),
]