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
    class Categories(models.TextChoices):
        WAX = 'Wax'
        GIPPURE = 'Gippure'
        SARI = 'Sari'
        TISSU = 'Tissu'
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    categorie = models.fields.CharField(max_length=100, choices=Categories.choices)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    new = models.fields.BooleanField(default=False)
    cat = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    upload = models.ImageField()

    

    def __str__(self):
        return f'{self.name} ( {self.description}) --> {self.categorie} {self.price}  '


        
