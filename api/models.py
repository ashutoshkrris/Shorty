from django.db import models


# Create your models here.

class APIKey(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    api_key = models.CharField(max_length=200)
    usage = models.IntegerField(default=0)
    expired = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.email}'
