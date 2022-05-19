from django import forms

from .models import Publication,Carousel, Schools

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

class CarruselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ('title', 'description', 'carousel_pic', 'ordenPublication', 'showbuton', 'nameButon', 'linkButon')

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'nameButon': forms.TextInput(attrs={'class': 'form-control'}),
                'linkButon': forms.TextInput(attrs={'class': 'form-control'}),
            }

class SchoolsForm(forms.ModelForm):
    class Meta:
        model = Schools
        fields = "__all__"

        widgets = {
                'UnidadAcademica': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
                'nombreCarrera': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'direction': forms.TextInput(attrs={'class': 'form-control'}),
                'urlSite': forms.TextInput(attrs={'class': 'form-control'}),
            }