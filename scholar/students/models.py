from django.db import models

# Create your models here.

class User(models.Model):
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=500)

class Notas(models.Model):
    nota1= models.IntegerField(max_length=100, default=0)
    nota2= models.IntegerField(max_length=500, default=0)
    nota3= models.IntegerField(max_length=500, default=0)
    defi= models.IntegerField(max_length=500, default=0)

