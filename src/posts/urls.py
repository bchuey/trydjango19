from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [

	url(r'^$', views.post_list, name='all'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^detail/$', views.post_detail, name='detail'),
    url(r'^update/$', views.post_update, name='update'),
    url(r'^delete/$', views.post_delete, name='delete'),
    # url(r'^posts/$', "<appname>.views.<function_name>"),

]