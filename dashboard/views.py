from django.shortcuts import render
from . forms import ProductForm
from . forms import CategorieForm
from . models import Product
from . models import Categorie 
from django.shortcuts import redirect

# Create your views here.

def dash(request):
	return render(request, 'dash.html')


def admin_categorie(request):
    categorie = Categorie.objects.all()
    return render(request, 'admin_categorie.html', {'categorie': categorie})
def admin_product(request):
    product = Product.objects.all()
    return render(request, 'admin_product.html', { 'product': product })

def admin_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'admin_details.html', {'product': product})
def admin_cat_detail(request, id):
    categorie = Categorie.objects.get(id=id)
    return render(request, 'admin_cat_detail.html', {'categorie': categorie})

def admin_all(request):
    categorie = Categorie.objects.all()
    product = Product.objects.all()
    return render(request, 'admin_all.html',{'categorie':categorie,'product':product })

def admin_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            print("********************",  form.errors)
            product = form.save()
            return redirect('admin_details', product.id)
        else:
            print("*************************************")
            print(form.errors)
            print("*************************************")
            form = ProductForm()
            return render(request, 'admin_create.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'admin_create.html', {'form': form})


def admin_create_cat(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            
            categorie = form.save()
            return redirect('admin_cat_detail', categorie.id)
        else:
            print("*************************************")
            print(form.errors)
            print("*************************************")
            form = CategorieForm()
            return render(request, 'admin_create_cat.html', {'form': form})  
    else:
        form = CategorieForm()
        return render(request, 'admin_create_cat.html', {'form': form})  



