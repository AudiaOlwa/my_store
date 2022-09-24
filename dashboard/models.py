from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    upload = models.ImageField()


    def __str__(self):
        return f'{self.name}({self.description}) '



class Product(models.Model):
   

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    new = models.fields.BooleanField(default=False)
    cat = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    upload = models.ImageField()

    

    def __str__(self):
        return f'{self.name} ( {self.description}) --> {self.price}  '


        
