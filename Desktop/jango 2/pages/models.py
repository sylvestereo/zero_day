from time import time
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=300)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title