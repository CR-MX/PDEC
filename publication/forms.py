from django import forms

from .models import Publication,Carousel,School, Objetivo, Mision, PlanDeTrabajo

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = "__all__"
        
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
                'nameButon': forms.Textarea(attrs={'class': 'form-control'}),
                'linkButon': forms.Textarea(attrs={'class': 'form-control'}),
            }

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"

        widgets = {
                'UnidadAcademica': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
                'nombreCarrera': forms.TextInput(attrs={'class': 'form-control'}),
                'direction': forms.TextInput(attrs={'class': 'form-control'}),
                'urlSite': forms.TextInput(attrs={'class': 'form-control'}),
                'cp_1_title': forms.TextInput(attrs={'class': 'form-control'}),
                'cp_1_description': forms.Textarea(attrs={'class': 'form-control'}),
                'cp_1_linkButon': forms.TextInput(attrs={'class': 'form-control'}),
                'cp_2_title': forms.TextInput(attrs={'class': 'form-control'}),
                'cp_2_description': forms.Textarea(attrs={'class': 'form-control'}),
                'cp_2_linkButon': forms.TextInput(attrs={'class': 'form-control'}),
                'cp_3_title': forms.TextInput(attrs={'class': 'form-control'}),
                'cp_3_description': forms.Textarea(attrs={'class': 'form-control'}),
                'cp_3_linkButon': forms.TextInput(attrs={'class': 'form-control'}),
                'content_1': forms.Textarea(attrs={'class': 'form-control'}),
                'content_2': forms.Textarea(attrs={'class': 'form-control'}),
                'content_3': forms.Textarea(attrs={'class': 'form-control'}),
            }

class ObjetivoForm(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = "__all__"
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'content1': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
        }
class MisionForm(forms.ModelForm):
    class Meta:
        model = Mision
        fields = "__all__"
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'content1': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
        }
class PlanDeTrabajoForm(forms.ModelForm):
    class Meta:
        model = PlanDeTrabajo
        fields = "__all__"
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
            'content1': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Campo Obligatorio'}),
        }