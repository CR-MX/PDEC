from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

# from django.conf import settings 
# from django.conf.urls.static import static


urlpatterns = [
    path('<int:id>/', views.Publicacion, name='publicacion'),
    path('crearPublicacion/', views.crearPublicacion, name='crearPublicacion'),
] 

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)