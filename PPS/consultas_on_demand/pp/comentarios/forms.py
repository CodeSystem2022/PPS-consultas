from django import forms
from .models import Comentarios

class FormComentarios(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['content_type', 'object_id', 'texto']
        widgets = {
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
            'texto': forms.Textarea()
        }
