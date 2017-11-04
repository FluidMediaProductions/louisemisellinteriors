from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='fabrics'),
    url(r'^add$', views.add, name='add_fabric'),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete, name='delete_fabric'),
    url(r'^estimate/(?P<id>[0-9]+)$', views.estimate, name='estimate_curtain'),
]
