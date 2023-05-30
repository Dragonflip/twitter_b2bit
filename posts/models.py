from django.contrib.auth.models import User
from django.db import models
import pathlib
import uuid


def path_file_name(instance, filename):
    fpath = pathlib.Path(filename)
    new_name = str(uuid.uuid1())
    return f"post_image/{new_name}{fpath.suffix}"


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=path_file_name, null=True)

    class Meta:
        ordering = ["-created_at"]
