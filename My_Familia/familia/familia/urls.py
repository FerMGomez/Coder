from django.contrib import admin
from django.urls import path
from familia.view import saludo, saludando, familia, lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('saludando/',saludando),
    path('familia/',familia),
    path('lista/',lista)
]
