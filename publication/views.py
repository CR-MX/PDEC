from django.shortcuts import render, redirect
from .forms import PublicationForm,CarruselForm, SchoolForm

# from publication import Publications
from publication.models import Publication,Carousel,School
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView
import os

def Publicacion(request, id):
    # print(id ,args,kwargs)
    
    article = Publication.objects.get(id=id)
    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {'article': article, 
                'all_article':all_article}
    # print(context)
    # article = Publication.objects.all()
    # print(public)
    return render(request, 'publicacion.html', context)

@login_required(login_url='eduacionapp:login')
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

@login_required(login_url='eduacionapp:login')
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
    all_publications = Publication.objects.all().order_by('-published')
    context = {
                'all_publications': all_publications,
    }
    return render(request, 'allPublications.html',context)

@login_required(login_url='eduacionapp:login')
def publicationAdmin(request):
    # all publications sort by desc
    all_publications = Publication.objects.all()
    context = {
                'all_publications': all_publications,
    }
    return render(request, 'publicationAdmin.html',context)

@login_required(login_url='eduacionapp:login')
def edicionPublication(request, id):
    article =Publication.objects.get(id=id)
    form = PublicationForm(instance=article)
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES , instance=article)
        if form.is_valid():
            image_path = article.publication_pic.path
            image_path2 = article.miniature_pic.path
            file_path=article.file1.path
            file_path2=article.file2.path
            file_path3=article.file3.path
            if os.path.exists(image_path):
                os.remove(image_path)
            elif os.path.exists(image_path2):
                os.remove(image_path2)
            elif os.path.exists(file_path):
                os.remove(file_path)
            elif os.path.exists(file_path2):
                os.remove(file_path2)
            elif os.path.exists(file_path3):
                os.remove(file_path3)
            form.save()
            return redirect('publication_app:publicationAdmin')
    context = {'article': form}
    return render(request, 'editarPublicacion.html', context)


@login_required(login_url='eduacionapp:login')
def eliminaPublicacion(request, id):
    publication = Publication.objects.get(id=id)
    if request.method == "POST":
        publication.delete()
        return redirect('publication_app:publicationAdmin')

    context = {'publication': publication}
    return render(request, 'eliminarPublicacion.html', context)

@login_required(login_url='eduacionapp:login')
def carruselAdmin(request):
    # all publications sort by desc
    all_carrusels = Carousel.objects.all()
    context = {
                'all_carrusels': all_carrusels,
    }
    return render(request, 'carruselAdmin.html',context)

@login_required(login_url='eduacionapp:login')
def edicionCarrusel(request, id):
    article =Carousel.objects.get(id=id)
    form = CarruselForm(instance=article)
    if request.method == 'POST':
        form = CarruselForm(request.POST, request.FILES , instance=article)
        if form.is_valid():
            image_path = article.carousel_pic.path
            if os.path.exists(image_path):
                os.remove(image_path)
            form.save()
            return redirect('publication_app:carruselAdmin')
    context = {'article': form}
    return render(request, 'editarCarrusel.html', context)

@login_required(login_url='eduacionapp:login')
def eliminaCarrusel(request, id):
    carrusel = Carousel.objects.get(id=id)
    if request.method == "POST":
        carrusel.delete()
        return redirect('publication_app:carruselAdmin')

    context = {'carrusel': carrusel}
    return render(request, 'eliminarCarrusel.html', context)

@login_required(login_url='eduacionapp:login')
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

@login_required(login_url='eduacionapp:login')
def escuelaAdmin(request):
    # all publications sort by desc
    all_school = School.objects.all()
    context = {
                'all_school': all_school,
    }
    return render(request, 'escuelaAdmin.html',context)

@login_required(login_url='eduacionapp:login')
def edicionEscuela(request, id):
    article =School.objects.get(id=id)
    #print(article)
    form = SchoolForm(instance=article)
    #print(form)
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            image_path = article.logo_pic.path
            image_path2 = article.miniature_pic.path
            image_path3 = article.carrusel_pic_1.path
            image_path4 = article.carrusel_pic_2.path
            image_path5 = article.carrusel_pic_3.path
            file_path=article.file1.path
            file_path2=article.file2.path
            file_path3=article.file3.path
            if os.path.exists(image_path):
                os.remove(image_path)
            elif os.path.exists(image_path2):
                os.remove(image_path2)
            elif os.path.exists(image_path3):
                os.remove(image_path3)
            elif os.path.exists(image_path4):
                os.remove(image_path4)
            elif os.path.exists(image_path5):
                os.remove(image_path5)
            elif os.path.exists(file_path):
                os.remove(file_path)
            elif os.path.exists(file_path2):
                os.remove(file_path2)
            elif os.path.exists(file_path3):
                os.remove(file_path3)

            form.save()
            return redirect('publication_app:escuelaAdmin')
    context = {'form': form}
    return render(request, 'editarEscuelas.html', context)

def schoolView(request, id):
    school = School.objects.get(id=id)
    context = {'school': school}
    #print(context)
    # article = Publication.objects.all()
    # print(public)
    return render(request, 'schoolView.html', context)

@login_required(login_url='eduacionapp:login')
def eliminaEscuela(request, id):
    school = School.objects.get(id=id)
    if request.method == "POST":
        school.delete()
        return redirect('publication_app:escuelaAdmin')

    context = {'school': school}
    return render(request, 'eliminarEscuela.html', context)


@staff_member_required(login_url='eduacionapp:login')
def adminCenter(request):
    
    return render(request, 'adminCenter.html')