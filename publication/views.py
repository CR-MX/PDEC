from django.shortcuts import render, redirect
from .forms import PublicationForm,CarruselForm, SchoolsForm

# from publication import Publications
from publication.models import Publication,Carousel,Schools


def Publicacion(request, id):
    # print(id ,args,kwargs)
    
    article = Publication.objects.get(id=id)
    context = {'article': article}
    print(context)
    # article = Publication.objects.all()
    # print(public)
    return render(request, 'publicacion.html', context)

def crearPublicacion(request):
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'landing.html')
    else:
        form = PublicationForm()
    return render(request, 'crearPublicacion.html', {'form': form})

def crearCarrusel(request):
    if request.method == "POST":
        form = CarruselForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'landing.html')
    else:
        form = CarruselForm()
    return render(request, 'crearCarrusel.html', {'form': form})

def allPublications(request):
    # all publications sort by desc
    all_publications = Publication.objects.all().filter(section='T')
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
            return redirect('eduacionapp:home')
    context = {'article': form}
    return render(request, 'editarPublicacion.html', context)

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
            return redirect('eduacionapp:home')
    context = {'form': form}
    print(context)
    return render(request, 'editarCarrusel.html', context)

def crearEscuela(request):
    if request.method == "POST":
        form = SchoolsForm(request.POST, request.FILES)
        print(form);
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'landing.html')
    else:
        form = SchoolsForm()
    return render(request, 'crearEscuela.html', {'form': form})