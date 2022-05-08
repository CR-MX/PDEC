from django.shortcuts import render
from .forms import PublicationForm,CarruselForm

# from publication import Publications
from publication.models import Publication,Carousel


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