from django.db import models

class Task(models.Model):
    judul = models.TextField()
    genre = models.TextField(default='')
