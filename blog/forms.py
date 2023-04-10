from django import forms
from blog.models import DataType

class DataTypeForm(forms.ModelForm):
    class Meta:
        model = DataType
        fields = ('name', 'description', 'example')

    widgets = {
        'description': forms.Textarea(attrs={'rows': 3}),
        'example': forms.Textarea(attrs={'rows': 3})
    }

from django import forms
from .models import MathOperator

class MathOperatorForm(forms.ModelForm):
    class Meta:
        model = MathOperator
        fields = ['name', 'symbol', 'description', 'example']
        labels = {
            'name': 'Nombre',
            'symbol': 'Símbolo',
            'description': 'Descripción',
            'example': 'Ejemplo',
        }
