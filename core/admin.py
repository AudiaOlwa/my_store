from django.contrib import admin
from .models import Product, Categorie

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'year_formed','cat')

class CategorieAdmin(admin.ModelAdmin):
	list_display = ('name', 'year_formed')

admin.site.register(Product, ProductAdmin)
admin.site.register(Categorie, CategorieAdmin)





