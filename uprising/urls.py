#-*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views import static

admin.autodiscover()

import blog.views

urlpatterns = [
	url(r'^$', blog.views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^artigo/(?P<artigo_id>\d+)$', blog.views.artigos),
    url(r'^media/(.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^contato/$', blog.views.contato),
    url(r'^comments/$', blog.views.comentarios),
]
