from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

def index(req):
    data = Task.objects.all()
    
    simpan = []
    for a in data :
        simpan.append({
            'judul': a.judul,
            'genre': a.genre 
        })

    return JsonResponse({
        'data': simpan
    }, safe=False)
