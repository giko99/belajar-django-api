from django.db import models

class Task(models.Model):
    judul = models.CharField(max_length=255)
    genre = models.TextField(default='')
