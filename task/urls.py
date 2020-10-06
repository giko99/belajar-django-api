from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),
]