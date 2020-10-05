from django.shortcuts import render
from django.urls import path
from . import views
# from .views import homePageView

urlpatterns = [
    # path('', homePageView, name='home'),
    path('', views.index),
    # path('<id>/', views.detail),
    # path('<id>/delete/', views.delete),
    # path('<id>/update/', views.update),
]