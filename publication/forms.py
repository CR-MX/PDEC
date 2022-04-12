#from django import forms
#from .models import Post

#class PublicationForm(forms.Form):
#    title = forms.CharField(help_text="Titulo")
#    author = forms.CharField(help_text="Autor")
#    description = forms.CharField(help_text="Descripcion")
#    content1 = forms.CharField(help_text="Contenido")

from django import forms

from .models import Publication

class PublicationForm(forms.ModelForm):

    class Meta:
        model = Publication
        fields = ('title', 'author', 'description', 'content1', 'content2','content3',)