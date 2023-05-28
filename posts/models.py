from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
