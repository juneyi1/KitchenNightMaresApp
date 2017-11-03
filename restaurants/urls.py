from django.conf.urls import url

from . import views

app_name = 'restaurants'
urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /1/
    url(r'^(?P<restaurant_id>[0-9]+)/$', views.detail, name='detail'),
]
