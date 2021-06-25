from django.db import models


# Create your models here.
class Camera(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=150)
    host = models.CharField(max_length=50)
    port = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}-{self.brand}'
