from operator import truediv

from django.db import models

# Create your models here.

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField()
