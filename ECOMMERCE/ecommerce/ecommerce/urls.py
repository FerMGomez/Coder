from django.contrib import admin
from django.urls import path

from ecommerce.view import segundo_template, saludo, bandas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('segundo_template/',segundo_template, name='segundo_template'),
    path('saludo/',saludo),
    path('bandas/',bandas)
]
