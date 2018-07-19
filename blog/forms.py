from django import forms
from blog.models import comentario

class FormComentario(forms.ModelForm):
	data = forms.DateField(
			widget=forms.DateInput(format='%d/%m/%Y'),
			input_formats=['%d/%m/%Y', '%d/%m/%y'])
	
	class Meta:
		model = comentario
		fields = ('nome', 'comentario', 'data')