from django.shortcuts import render
from .forms import PublicationForm

# from publication import Publications
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
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'landing.html')
    else:
        form = PublicationForm()
    return render(request, 'crearPublicacion.html', {'form': form})