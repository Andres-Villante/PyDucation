from django import forms
from blog.models import DataType, MathOperator, Function, PracticeExercise, Post, Response


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
    class Meta:
        model = Function
        fields = ['name', 'description', 'example']

class PracticeExerciseForm(forms.ModelForm):
    class Meta:
        model = PracticeExercise
        fields = ['title', 'description', 'level']
        labels = {'title': 'Título', 'description': 'Descripción', 'level': 'Nivel'}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }