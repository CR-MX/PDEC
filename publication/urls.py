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
    path('carruselAdmin/',views.carruselAdmin, name='carruselAdmin'),
    path('edicionCarrusel/<int:id>/',views.edicionCarrusel, name='edicionCarrusel'),
    path('crearEscuela/', views.crearEscuela, name='crearEscuela'),
] 

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)