from django.contrib import admin
from blog.models import artigo
from blog.models import comentario
admin.site.register(artigo)
admin.site.register(comentario)