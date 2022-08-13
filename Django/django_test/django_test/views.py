from urllib import request
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request):
    return HttpResponse('Hola Mundo....!!!')

def gabu(request):
    dia = datetime.today().date()
    return HttpResponse(f'La Gabuuuuuuuuuuu....{dia}!!!')

def putoviejo(request):
    dia=datetime.today()
    return HttpResponse('Te llamo un UBER o DIDI????....!!!')

def putojoven(request):
    dia=datetime.today()
    return HttpResponse('Me encanta la pija SUCIA....!!!')

def plantilla(request):
    return render(request,'plantilla.html',context={})