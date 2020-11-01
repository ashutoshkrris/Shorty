from django.db import models

# Create your models here.
class short_url(models.Model):
    original_URL = models.URLField(blank=False)
    short_Query = models.CharField(blank=False, max_length=255)
    