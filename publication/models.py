from pickle import TRUE
from turtle import title
from django.db import models

class Publication(models.Model):
    
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    content1 = models.TextField(max_length=1000)
    content2 = models.TextField(max_length=1000, null=True, blank=True)
    content3 = models.TextField(max_length=1000, null=True, blank=True)
    background_pic = models.ImageField(null=True,blank=True)
    publication_pic = models.ImageField(null=True,blank=True)
    miniature_pic = models.ImageField(null=True,blank=True)
    section_p =(
                ('n','none'),
                ('F','First_Section'),
                ('1','Second_Sec_1'),
                ('2','Second_Sec_2'),
                ('3','Second_Sec_3'),
                ('T','Third_Section')
                )
    section = models.CharField(max_length=1, choices=section_p, blank=True, default='n')

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
                ('3','Carusel 3')
                )
    ordenPublication = models.CharField(max_length=1, choices=activa, blank=True, default='D')
    visible =(
                ('A','Activado'),
                ('D','Desactivado')
                )
    showbuton = models.CharField(max_length=1, choices=visible, blank=True, default='D')
    nameButon = models.TextField(max_length=500, null=True, blank=True)
    linkButon = models.TextField(max_length=500, null=True, blank=True)
    def __str__(self) :
        return "(No.%i) %s" % (self.id, self.title)