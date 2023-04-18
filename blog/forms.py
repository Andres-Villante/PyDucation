from django import forms
from blog.models import Profile, User, DataType, MathOperator, Function, PracticeExercise, Post, Response
from django_countries.fields import CountryField
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name', 'nationality', 'bio', 'profile_pic')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].required = True


class DataTypeForm(forms.ModelForm):
    class Meta:
        model = DataType
        fields = ('name', 'description', 'detailed_description', 'example')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'detailed_description': forms.TextInput(attrs={'class': 'form-control'}),
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