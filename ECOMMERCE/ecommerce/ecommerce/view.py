from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    return HttpResponse('HOLAAAAAA MUNDOOOO')

def segundo_template(request):
    today = datetime.now().date
    contex = {
        'name':'Fernando',
        'last_name':'Gomez',
        'carro':'RENAULT',
        'today':today
    }
    return render(request,'template_2.html', context=contex)

def bandas(request):
    today = datetime.now().date
    contex = {
        'banda':['MegadetH','MetallicA','AnthraX','SlayeR'],
        'today':today
    }
    return render(request,'template_lista.html', context=contex)