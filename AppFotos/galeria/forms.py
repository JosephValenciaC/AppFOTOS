from django import forms
from .models import Nota, Foto

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['contenido']

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['imagen']

from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre']  # Campos del formulario que deseas incluir
