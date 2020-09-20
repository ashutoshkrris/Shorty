from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class shorturl(models.Model):
    originalURL = models.URLField(blank=False)
    shortQuery = models.CharField(blank=False, max_length=8)
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)