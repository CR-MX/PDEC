from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

# from django.conf import settings 
# from django.conf.urls.static import static

app_name='publication_app'
urlpatterns = [
    path('<int:id>/', views.Publicacion, name='publication'),
    path('crearPublicacion/', views.crearPublicacion, name='crearPublicacion'),
    path('crearCarrusel/', views.crearCarrusel, name='crearCarrusel'),
    path('all/', views.allPublications, name='allPublications'),
    path('publicationAdmin/',views.publicationAdmin, name='publicationAdmin'),
    path('edicionPublication/<int:id>/',views.edicionPublication, name='edicionPublication'),
    path('eliminaPublicacion/<int:id>/', views.eliminaPublicacion, name='eliminaPublicacion'),
    path('carruselAdmin/',views.carruselAdmin, name='carruselAdmin'),
    path('edicionCarrusel/<int:id>/',views.edicionCarrusel, name='edicionCarrusel'),
    path('eliminaCarrusel/<int:id>/', views.eliminaCarrusel, name='eliminaCarrusel'),
    path('crearEscuela/', views.crearEscuela, name='crearEscuela'),
    path('escuelaAdmin/',views.escuelaAdmin, name='escuelaAdmin'),
    path('edicionEscuela/<int:id>/',views.edicionEscuela, name='edicionEscuela'),
    path('eliminaEscuela/<int:id>/', views.eliminaEscuela, name='eliminaEscuela'),
    path('schoolView/<int:id>/',views.schoolView, name='schoolView'),
    path('adminCenter/',views.adminCenter, name='adminCenter'),
    # nuevos campos
    path('crearObjetivo/', views.crearObjetivo, name='crearObjetivo'),
    path('crearMision/', views.crearMision, name='crearMision'),
    path('crearPlanDeTrabajo/', views.crearPlanDeTrabajo, name='crearPlanDeTrabajo'),
    # index
    path('indexObjetivo/',views.indexObjetivo, name='indexObjetivo'),
    path('indexMision/',views.indexMision, name='indexMision'),
    path('indexPlanDeTrabajo/',views.indexPlanDeTrabajo, name='indexPlanDeTrabajo'),
    # editar nuevos campos
    path('editObjetivo/<int:id>/',views.editObjetivo, name='editObjetivo'),
    path('editMision/<int:id>/',views.editMision, name='editMision'),
    path('editPlanDeTrabajo/<int:id>/',views.editPlanDeTrabajo, name='editPlanDeTrabajo'),
    #  eliminar
    path('eliminarObjetivo/<int:id>/', views.eliminarObjetivo, name='eliminarObjetivo'),
    path('eliminarMision/<int:id>/', views.eliminarMision, name='eliminarMision'),
    path('eliminarPlanDeTrabajo/<int:id>/', views.eliminarPlanDeTrabajo, name='eliminarPlanDeTrabajo'),
    # navbar
    path('navObjetivo/', views.navObjetivo, name='navObjetivo'),
    path('navMision/', views.navMision, name='navMision'),
    path('navPlanDeTrabajo/', views.navPlanDeTrabajo, name='navPlanDeTrabajo'),
    # Previsualizar 
    path('preObjetivo/<int:id>/', views.preObjetivo, name='preObjetivo'),
    path('preMision/<int:id>/', views.preMision, name='preMision'),
    path('prePlanDeTrabajo/<int:id>/', views.prePlanDeTrabajo, name='prePlanDeTrabajo'),
] 

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)