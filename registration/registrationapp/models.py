from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, default="")
    password = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.username