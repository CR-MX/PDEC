from pickle import TRUE
from turtle import title
from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=250, help_text="Introduce el titulo")
    author = models.CharField(max_length=250, help_text="Introduce el autor")
    description = models.CharField(max_length=250, help_text="Introduce la descripcion")
    content1 = models.TextField(max_length=1000, help_text="Introduce el contenido 1")
    content2 = models.TextField(max_length=1000, null=True, blank=True)
    content3 = models.TextField(max_length=1000, null=True, blank=True)
    background_pic = models.ImageField(null=True,blank=True)
    publication_pic = models.ImageField(null=True,blank=True)
    miniature_pic = models.ImageField(null=True,blank=True)
    
    def __str__(self) :
        return "(No.%i) %s by %s" % (self.id, self.title, self.author)

