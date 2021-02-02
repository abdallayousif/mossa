from django.db import models

# Create your models here.
class Products(models.Model):
    ProName = models.CharField(max_length=100)
