from django import forms

from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'author', 'description', 'content1', 'content2', 'content3', 'background_pic', 'publication_pic', 'miniature_pic', 'section')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'content1': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'content2': forms.Textarea(attrs={'class': 'form-control'}),
            'content3': forms.Textarea(attrs={'class': 'form-control'}),
        }
        