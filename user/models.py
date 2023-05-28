from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to=None)

