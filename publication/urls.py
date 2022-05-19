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
    path('schoolView/<int:id>/',views.obtenerEscuela, name='schoolView'),
] 

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)