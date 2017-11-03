from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='wallpapers'),
    url(r'^visualize/(?P<id>[0-9]+)$', views.visualize, name='visualize')
]
