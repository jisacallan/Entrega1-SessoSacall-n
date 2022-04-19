from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class UserAvatar(models.Model):
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(null=True)
    more_description = models.CharField(max_length=100, default='Some String')