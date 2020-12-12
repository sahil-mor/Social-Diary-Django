from django import forms
from .models import BlogsModel
class BlogsForm(forms.ModelForm):
    class Meta:
        model = BlogsModel
        fields = ['headline','decription','photo']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Headline'}),
            'decription': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Description'}),
        }