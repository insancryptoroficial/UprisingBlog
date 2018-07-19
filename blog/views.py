# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from blog.models import artigo
from blog.forms import FormComentario
from blog.models import comentario
from django.core.mail import send_mail

def home(request):
	lista_itens = artigo.objects.all()
	return render(request, "artigo_archive.html",
				{'lista_itens':lista_itens})

def artigos(request, artigo_id):
	lista_artigo = artigo.objects.get(id=artigo_id)
	return render_to_response("artigo.html", locals(), context_instance=RequestContext(request))

def comentarios(request):
	if request.method == 'POST':
		form = FormComentario(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("/comments/")
	else:
		form = FormComentario()

	return render(request, "comentario.html", {'form':form})

def contato(request):
	if request.method == 'POST':
		form = FormContato(request.POST)

		if form.is_valid():
			form.enviar()
			mostrar = 'Contato enviado!'
	else:
		form = FormContato()

	return render_to_response('contato.html', locals(), context_instance=RequestContext(request))

class FormContato(forms.Form):
	nome = forms.CharField(max_length=50)
	email = forms.EmailField(required=False)
	mensagem = forms.Field(widget=forms.Textarea)
	def enviar(self):
		titulo = 'Mensagem enviada pelo site'
		destino = 'isaiasmoraes2000@gmail.com'
		texto = """
		Nome: %(nome)s
		E-mail: %(email)s
		Mensagem:
		%(mensagem)s
		""" % self.cleaned_data

		send_mail(
			subject=titulo,
			message=texto,
			from_email=destino,
			recipient_list=[destino],
			)
