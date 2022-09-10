from django.forms import models
from . models import Product
from . models import Categorie
from django import forms

class ContactForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   password=forms.CharField()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' 
        
class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__' 
                