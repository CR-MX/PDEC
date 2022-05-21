from django.shortcuts import render, redirect
from .forms import PublicationForm,CarruselForm, SchoolForm

# from publication import Publications
from publication.models import Publication,Carousel,School

from django.views.generic import ListView

def Publicacion(request, id):
    # print(id ,args,kwargs)
    
    article = Publication.objects.get(id=id)
    all_article = Publication.objects.all()
    all_article = all_article[0:6]
    context = {'article': article, 
                'all_article':all_article}
    # print(context)
    # article = Publication.objects.all()
    # print(public)
    return render(request, 'publicacion.html', context)

def crearPublicacion(request):
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('publication_app:publicationAdmin')
            
    else:
        form = PublicationForm()
    return render(request, 'crearPublicacion.html', {'form': form})

def crearCarrusel(request):
    if request.method == "POST":
        form = CarruselForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('publication_app:carruselAdmin')
    else:
        form = CarruselForm()
    return render(request, 'crearCarrusel.html', {'form': form})

def allPublications(request):
    # all publications sort by desc
    all_publications = Publication.objects.all()
    context = {
                'all_publications': all_publications,
    }
    return render(request, 'allPublications.html',context)

def publicationAdmin(request):
    # all publications sort by desc
    all_publications = Publication.objects.all()
    context = {
                'all_publications': all_publications,
    }
    return render(request, 'publicationAdmin.html',context)

def edicionPublication(request, id):
    article =Publication.objects.get(id=id)
    form = PublicationForm(instance=article)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('publication_app:publicationAdmin')
    context = {'article': form}
    return render(request, 'editarPublicacion.html', context)

def eliminaPublicacion(request, id):
    publication = Publication.objects.get(id=id)
    if request.method == "POST":
        publication.delete()
        return redirect('publication_app:publicationAdmin')

    context = {'publication': publication}
    return render(request, 'eliminarPublicacion.html', context)

def carruselAdmin(request):
    # all publications sort by desc
    all_carrusels = Carousel.objects.all()
    context = {
                'all_carrusels': all_carrusels,
    }
    return render(request, 'carruselAdmin.html',context)

def edicionCarrusel(request, id):
    article =Carousel.objects.get(id=id)
    print(article)
    form = CarruselForm(instance=article)
    #print(form)
    if request.method == 'POST':
        form = CarruselForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('publication_app:carruselAdmin')
    context = {'form': form}
    print(context)
    return render(request, 'editarCarrusel.html', context)

def eliminaCarrusel(request, id):
    carrusel = Carousel.objects.get(id=id)
    if request.method == "POST":
        carrusel.delete()
        return redirect('publication_app:carruselAdmin')

    context = {'carrusel': carrusel}
    return render(request, 'eliminarCarrusel.html', context)

def crearEscuela(request):
    if request.method == "POST":
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            
            return redirect('publication_app:escuelaAdmin')

    else:
        form = SchoolForm()
    return render(request, 'crearEscuela.html', {'form': form})


def escuelaAdmin(request):
    # all publications sort by desc
    all_school = School.objects.all()
    context = {
                'all_school': all_school,
    }
    return render(request, 'escuelaAdmin.html',context)


def edicionEscuela(request, id):
    article =School.objects.get(id=id)
    #print(article)
    form = SchoolForm(instance=article)
    #print(form)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('publication_app:escuelaAdmin')
    context = {'form': form}
    print(context)
    return render(request, 'editarEscuelas.html', context)

def schoolView(request, id):
    school = School.objects.get(id=id)
    context = {'school': school}
    #print(context)
    # article = Publication.objects.all()
    # print(public)
    return render(request, 'schoolView.html', context)

def eliminaEscuela(request, id):
    school = School.objects.get(id=id)
    if request.method == "POST":
        school.delete()
        return redirect('publication_app:escuelaAdmin')

    context = {'school': school}
    return render(request, 'eliminarEscuela.html', context)

def adminCenter(request):
    # all publications sort by desc
    # all_publications = Publication.objects.all().filter(section='T')
    # context = {
    #             'all_publications': all_publications,
    # }
    # return render(request, 'adminCenter.html',context)
    return render(request, 'adminCenter.html')
