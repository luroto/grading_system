from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
	class Meta:
		model = Nota
		fields = ['student_id', 'area_id', 'grade', 'grade_description', 'creado']
