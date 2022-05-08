from django.contrib import admin
from django.urls import path, include

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('educuaz/publication/', include('publication.urls', namespace='publication_app')),
    path('educuaz/', include('usuarios.urls', namespace='eduacionapp')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
