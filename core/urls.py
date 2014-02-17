# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from core import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='prots'),
    url(r'forms/$', views.formulario, name='core_forms'),
    url(r'forms/(?P<id>\d+)/$', views.detail, name='core_detail'),
)