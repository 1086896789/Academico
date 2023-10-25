from django.db import models

# Create your models here.

class User(models.Model):
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=500)

class Notas(models.Model):
    nota1= models.CharField(max_length=100)
    nota2= models.CharField(max_length=500)
    nota3= models.CharField(max_length=500)

