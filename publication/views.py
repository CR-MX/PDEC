from django.shortcuts import render
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