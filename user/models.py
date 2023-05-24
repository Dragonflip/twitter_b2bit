from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    data_nascimento = models.DateField()
    profile_picture = models.ImageField(upload_to=None)
