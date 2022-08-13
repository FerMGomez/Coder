from django.contrib import admin
from django.urls import path


from django_test.views import saludo, gabu, plantilla

 



urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/", saludo, name ='view_de_saludo'),
    path('gabu/', gabu, name='gabu'),
    path("plantilla/", plantilla, name='plantilla')
]
