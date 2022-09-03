from django.db import models

# Create your models here.



class Customer(models.Model):
    name = models.CharField(max_length=300, unique=True)
    title=models.CharField(max_length=300, unique=True)
    body=models.TextField(blank=True)
    address=models.CharField(max_length=300, unique=True)
    phone=models.CharField(max_length=300, unique=True)
    state=models.CharField(max_length=55, unique=True)
    image_url=models.URLField(max_length=300, unique=True)


    def __str__(self):
        return self.name