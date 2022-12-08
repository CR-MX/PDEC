from django.shortcuts import render, redirect
from .forms import MisionForm, PlanDeTrabajoForm, PublicationForm,CarruselForm, ReglamentoForm, SchoolForm, ObjetivoForm

# from publication import Publications
from publication.models import Publication, Carousel, Reglamento, School, Objetivo, Mision, PlanDeTrabajo
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView
import os

def Publicacion(request, id):
    article = Publication.objects.get(id=id)
    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {'article': article, 
                'all_article':all_article}

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

@staff_member_required(login_url='eduacionapp:login')
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
            form.save()
            return redirect('publication_app:publicationAdmin')
    context = {'form': form}
    return render(request, 'editarPublicacion.html', context)


@login_required(login_url='eduacionapp:login')
def eliminaPublicacion(request, id):
    publication = Publication.objects.get(id=id)
    if request.method == "POST":
        publication.delete()
        return redirect('publication_app:publicationAdmin')

    context = {'publication': publication}
    return render(request, 'eliminarPublicacion.html', context)

@staff_member_required(login_url='eduacionapp:login')
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
            form.save()
            return redirect('publication_app:carruselAdmin')
    context = {'form': form}
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

@staff_member_required(login_url='eduacionapp:login')
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
            form.save()
            return redirect('publication_app:escuelaAdmin')
    context = {'form': form}
    return render(request, 'editarEscuelas.html', context)

def schoolView(request, id):
    school = School.objects.get(id=id)
    
    # second section img rectangle speccific  1, 2, 3
    s_sec1 = Publication.objects.all().filter(Universidad=school.Universidad, section='1')
    s_sec1 = s_sec1[0:1]
    s_sec2 = Publication.objects.all().filter(Universidad=school.Universidad, section='2')
    s_sec2 = s_sec2[0:1]
    s_sec3 = Publication.objects.all().filter(Universidad=school.Universidad, section='3')
    s_sec3 = s_sec3[0:1]
    # third section img square
    t_sec = Publication.objects.all().filter( Universidad=school.Universidad, section='T')
    t_sec = t_sec[0:3]
    context = {'school': school,
                's_sec1': s_sec1,
                's_sec2': s_sec2,
                's_sec3': s_sec3,
                't_sec': t_sec
                }

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
# crear cosas---------------------------------------------------------------
@login_required(login_url='eduacionapp:login')
def crearObjetivo(request):
    if request.method == "POST":
        form = ObjetivoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            print(post)
            post.save()
            return redirect('publication_app:indexObjetivo')
    else:
        form = ObjetivoForm()
    return render(request, 'crearObjetivo.html', {'form': form})
    
@login_required(login_url='eduacionapp:login')
def crearMision(request):
    print(request.method)    
    if request.method == "POST":
        form = MisionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('publication_app:publicationAdmin')
            
    else:
        form = MisionForm()
    return render(request, 'crearMision.html', {'form': form})
    
@login_required(login_url='eduacionapp:login')
def crearPlanDeTrabajo(request):
    if request.method == "POST":
        form = PlanDeTrabajoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('publication_app:publicationAdmin')
            
    else:
        form = PlanDeTrabajoForm()
    return render(request, 'crearPlanDeTrabajo.html', {'form': form})

# vistas en las que mostramos los datos ----------------------------------------------------

@staff_member_required(login_url='eduacionapp:login')
def indexObjetivo(request):
    objetivos = Objetivo.objects.all()
    context = {
                'objetivos': objetivos,
    }
    return render(request, 'indexObjetivo.html',context)

@staff_member_required(login_url='eduacionapp:login')
def indexMision(request):
    misiones = Mision.objects.all()
    context = {
                'misiones': misiones,
    }
    return render(request, 'indexMision.html',context)

@staff_member_required(login_url='eduacionapp:login')
def indexPlanDeTrabajo(request):
    planesDeTrabajo = PlanDeTrabajo.objects.all()
    print(planesDeTrabajo)
    context = {
                'planesDeTrabajo': planesDeTrabajo,
    }
    return render(request, 'indexPlanDeTrabajo.html',context)
# edit to new 3 -----------------------------------------------------------------------------
@login_required(login_url='eduacionapp:login')
def editObjetivo(request, id):
    article =Objetivo.objects.get(id=id)
    form = ObjetivoForm(instance=article)
    if request.method == 'POST':
        form = ObjetivoForm(request.POST, request.FILES , instance=article)
        if form.is_valid():
            form.save()
            return redirect('publication_app:indexObjetivo')
    context = {'form': form}
    return render(request, 'crearObjetivo.html', context)

@login_required(login_url='eduacionapp:login')
def editMision(request, id):
    article =Mision.objects.get(id=id)
    form = MisionForm(instance=article)
    if request.method == 'POST':
        form = MisionForm(request.POST, request.FILES , instance=article)
        if form.is_valid():
            form.save()
            return redirect('publication_app:indexMision')
    context = {'form': form}
    return render(request, 'crearMision.html', context)

@login_required(login_url='eduacionapp:login')
def editPlanDeTrabajo(request, id):
    article =PlanDeTrabajo.objects.get(id=id)
    form = PlanDeTrabajoForm(instance=article)
    if request.method == 'POST':
        form = PlanDeTrabajoForm(request.POST, request.FILES , instance=article)
        if form.is_valid():
            form.save()
            return redirect('publication_app:indexPlanDeTrabajo')
    context = {'form': form}
    return render(request, 'crearPlanDeTrabajo.html', context)

# Eliminar las mismas cosas --------------------------------------------------------------------

@login_required(login_url='eduacionapp:login')
def eliminarObjetivo(request, id):
    objetivo = Objetivo.objects.get(id=id)
    if request.method == "POST":
        objetivo.delete()
        return redirect('publication_app:indexObjetivo')

    context = {'publication': objetivo}
    return render(request, 'eliminarObjetivo.html', context)

@login_required(login_url='eduacionapp:login')
def eliminarMision(request, id):
    publication = Mision.objects.get(id=id)
    if request.method == "POST":
        publication.delete()
        return redirect('publication_app:indexMision')

    context = {'publication': publication}
    return render(request, 'eliminarMision.html', context)

@login_required(login_url='eduacionapp:login')
def eliminarPlanDeTrabajo(request, id):
    publication = PlanDeTrabajo.objects.get(id=id)
    if request.method == "POST":
        publication.delete()
        return redirect('publication_app:indexPlanDeTrabajo')

    context = {'publication': publication}
    return render(request, 'eliminarPlanDeTrabajo.html', context)
# nav --------------------------------------

def navObjetivo(request):
    article = Objetivo.objects.all().filter(Activo='S').first()
    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {
        'article': article, 
        'all_article':all_article
    }
    return render(request, 'vistasNav.html', context)

def navMision(request):
    article = Mision.objects.all().filter(Activo='S').first()

    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {
        'article': article, 
        'all_article':all_article
    }
    return render(request, 'vistasNav.html', context)
    
def navPlanDeTrabajo(request):
    article = PlanDeTrabajo.objects.all().filter(Activo='S').first()
    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {
        'article': article, 
        'all_article':all_article
    }
    return render(request, 'vistasNav.html', context)

    # previsualizar las cosas

def preObjetivo(request, id):
    article = Objetivo.objects.get(id=id)
    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {'article': article, 
                'all_article':all_article}

    return render(request, 'vistasNav.html', context)

def preMision(request, id):
    article = Mision.objects.get(id=id)
    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {'article': article, 
                'all_article':all_article}

    return render(request, 'vistasNav.html', context)

def prePlanDeTrabajo(request, id):
    article = PlanDeTrabajo.objects.get(id=id)
    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {'article': article, 
                'all_article':all_article}

    return render(request, 'vistasNav.html', context)
# Reglamentación ----------------------------------------------------------------------------------------------------------------
@staff_member_required(login_url='eduacionapp:login')
def indexReglamento(request):
    regalamento = Reglamento.objects.all()
    context = {
                'regalamento': regalamento,
    }
    return render(request, 'indexReglamento.html',context)

@login_required(login_url='eduacionapp:login')
def crearReglamento(request):
    if request.method == "POST":
        form = ReglamentoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            print(post)
            post.save()
            return redirect('publication_app:indexReglamento')
    else:
        form =ReglamentoForm()
    return render(request, 'crearReglamento.html', {'form': form})

@login_required(login_url='eduacionapp:login')
def editReglamento(request, id):
    article =Reglamento.objects.get(id=id)
    form = ReglamentoForm(instance=article)
    if request.method == 'POST':
        form = ReglamentoForm(request.POST, request.FILES , instance=article)
        if form.is_valid():
            form.save()
            return redirect('publication_app:indexReglamento')
    context = {'form': form}
    return render(request, 'crearReglamento.html', context)

@login_required(login_url='eduacionapp:login')
def eliminarReglamento(request, id):
    regalamento = Reglamento.objects.get(id=id)
    if request.method == "POST":
        regalamento.delete()
        return redirect('publication_app:indexReglamento')

    context = {'publication': regalamento}
    return render(request, 'eliminarReglamento.html', context)

def navReglamento(request):
    article = Reglamento.objects.all().filter(Activo='S').first()
    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {
        'article': article, 
        'all_article':all_article
    }
    return render(request, 'vistasNav.html', context)
# creacion ----------------------------------------------------------------------------------------------------------------------

def preReglamento(request, id):
    article = Reglamento.objects.get(id=id)
    all_article = Publication.objects.all().order_by('-published')
    all_article = all_article[0:6]
    context = {'article': article, 
                'all_article':all_article}

    return render(request, 'vistasNav.html', context)