from ast import If, Str
from django.shortcuts import render
# from publication import Publications
from publication.models import Publication
from .forms import PublicationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, request


#importa los grupos que tienen diferentes permisos
from django.contrib.auth.models import Group
#Desde la otra aplicación
from publication.models import Publication

def Publicacion(request, id):
    # print(id ,args,kwargs)
    
    article = Publication.objects.get(id=id)
    context = {'article': article}
    print(context)
    # article = Publication.objects.all()
    # print(public)
    return render(request, 'publicacion.html', context)


def crearPublicacion(request):
    form = PublicationForm()
    return render(request, 'crearPublicacion.html', {'form': form})

def crearPublicacion(request):
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'landing.html')
    else:
        form = PublicationForm()
    return render(request, 'crearPublicacion.html', {'form': form})