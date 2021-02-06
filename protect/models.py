from django.db import models

# Create your models here.


class Products(models.Model):
    ProName = models.CharField(max_length=100)
    Description = models.TextField()
    Price = models.IntegerField()
    Image = models.ImageField(null=True, blank=True,)
    Category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.ProName



class Category(models.Model):
    CatName = models.CharField(max_length=15)

    def __str__(self):
        return self.CatName
