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
