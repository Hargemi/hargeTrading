
from django.contrib import admin
from django.urls import path
from django.urls import path, include
# Añade estas importaciones:
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Curso.urls')),  # Include URLs from the Curso app
    path('Cursofree/', include('Cursofree.urls')),  # Include URLs from the Curso app
    path('Cursopago/', include('Cursopago.urls')), 
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
]

