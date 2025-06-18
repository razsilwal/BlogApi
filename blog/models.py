from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title