from django import forms
from blog.models import DataType, MathOperator, Function
from django.utils.text import Truncator


class DataTypeForm(forms.ModelForm):
    class Meta:
        model = DataType
        fields = ('name', 'description', 'example')

    widgets = {
        'description': forms.Textarea(attrs={'rows': 3}),
        'example': forms.Textarea(attrs={'rows': 3})
    }

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

class FunctionForm(forms.ModelForm):
    description = models.TextField('Descripción', help_text='Ingrese una descripción para la función', blank=True, null=True)
    example = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Function
        fields = ['name', 'description', 'example']
