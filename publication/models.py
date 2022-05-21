from pickle import TRUE
from turtle import title
from django.db import models
from django.utils import timezone

class Publication(models.Model):
    
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    content1 = models.TextField(max_length=2000)
    content2 = models.TextField(max_length=2000, null=True, blank=True)
    content3 = models.TextField(max_length=2000, null=True, blank=True)
    
    publication_pic = models.ImageField(null=True,blank=True)
    miniature_pic = models.ImageField(null=True,blank=True)
    section_p =(
                ('n','none'),
                ('1','Segunda_Sec_1'),
                ('2','Segunda_Sec_2'),
                ('3','Segunda_Sec_3'),
                ('T','Tercera_Section')
                )
    section = models.CharField(max_length=1, choices=section_p, blank=True, default='n')
    published = models.DateField(auto_now_add=True)
    file1 = models.FileField(null=True,blank=True)
    file2 = models.FileField(null=True,blank=True)
    file3 = models.FileField(null=True,blank=True)

    def __str__(self) :
        return "(No.%i) %s by %s" % (self.id, self.title, self.author)
        
class Carousel(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500, null=True, blank=True)
    carousel_pic = models.ImageField(null=True,blank=True)
    activa =(
                ('N','No visible'),
                ('1','Carusel 1'),
                ('2','Carusel 2'),
                ('3','Carusel 3'),
                ('4','notas')
                )
    ordenPublication = models.CharField(max_length=1, choices=activa, blank=True, default='D')
    visible =(
                ('A','Activado'),
                ('D','Desactivado')
                )
    showbuton = models.CharField(max_length=1, choices=visible, blank=True, default='D')
    nameButon = models.TextField(max_length=250, null=True, blank=True)
    linkButon = models.TextField(max_length=1000, null=True, blank=True)
    def __str__(self) :
        return "(No.%i) %s" % (self.id, self.title)

class School(models.Model):
     UnidadAcademica = models.CharField(max_length=250)
     nombreCarrera = models.CharField(max_length=250)
     logo_pic = models.ImageField(null=True,blank=True)
     direction=models.CharField(max_length=500)
     urlSite = models.CharField(max_length=500)
     miniature_pic = models.ImageField(null=True,blank=True)
     carrusel_pic_1 = models.ImageField(null=True,blank=True)
     carrusel_pic_2 = models.ImageField(null=True,blank=True)
     carrusel_pic_3 = models.ImageField(null=True,blank=True)
     visible =(('A','Activado'),
                ('D','Desactivado'))
     content_1 = models.TextField(max_length=2000, null=True, blank=True)
     content_2 = models.TextField(max_length=2000, null=True, blank=True)
     content_3 = models.TextField(max_length=2000, null=True, blank=True)
     file1 = models.FileField(null=True,blank=True)
     file2 = models.FileField(null=True,blank=True)
     file3 = models.FileField(null=True,blank=True)
     def __str__(self) :
        return "(No.%i) %s" % (self.id, self.nombreCarrera)