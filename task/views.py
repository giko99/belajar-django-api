from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from .models import Task

def index(req):
    data = Task.objects.all()
    
    simpan = []
    for a in data :
        simpan.append(model_to_dict(a))

    return JsonResponse({
        'data': simpan
    }, safe=False)

def create(req):
    if req.method == 'POST':
        data_byte = req.body
        data_string = str(data_byte, 'utf-8')
        data = json.loads(data_string)

        a = Task.objects.create(
            judul=data['judul'], 
            genre=data['genre'])
        return JsonResponse({
            'data': model_to_dict(a),
        })

def delete(req, id):
    if req.method == 'DELETE':
        a = Task.objects.filter(pk=id).delete()
    return JsonResponse({
            'msg': 'data sudah terhapus'
        })

def detail(req, id):
    if req.method == 'GET':
        a = Task.objects.filter(pk=id).first()
    return JsonResponse({
        'data': model_to_dict(a),
    })

def update(req, id):
    if req.method == 'PUT':
        data_byte = req.body
        data_string = str(data_byte,'utf-8')
        data = json.loads(data_string)

        a = Task.objects.filter(pk=id).update(
            judul=data['judul'], 
            genre=data['genre']
        )
        a = Task.objects.filter(pk=id).first()

        return JsonResponse({
            'data': model_to_dict(a),
        })