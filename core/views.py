from django.shortcuts import render
from . forms import ContactForm
from . forms import ProductForm
from . forms import CategorieForm
from . models import Product
from . models import Categorie 
from django.shortcuts import redirect
from django.core.mail import send_mail

#-----------------------

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            return redirect('confirm')
    else:
        form = ContactForm()
    return render(request, "contact.html",{'form': form})

def home(request):
    categorie = Categorie.objects.all()
    product = Product.objects.all()
    return render(request, 'all.html',{'categorie':categorie,'product':product })

    

    

def categorie(request):
    categorie = Categorie.objects.all()
    return render(request, 'categorie.html', {'categorie': categorie})
def product(request):
    product = Product.objects.all()
    return render(request, 'product.html', { 'product': product })

def details(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'details.html', {'product': product})
def cat_detail(request, id):
    categorie = Categorie.objects.get(id=id)
    return render(request, 'cat_detail.html', {'categorie': categorie})
   
def confirm(request):
    return render(request, 'confirm.html')

#def create(request):
    #if request.method == 'POST':
     #   form = ProductForm(request.POST)
      #  if form.is_valid():
      #      print("********************",  form.errors)
      #      product = form.save()
      #      return redirect('details', product.id)
      #  else:
      #      print("*************************************")
      #      print(form.errors)
      #      print("*************************************")
      #      form = ProductForm()
      #      return render(request, 'create.html', {'form': form})
   # else:
   #     form = ProductForm()
   #     return render(request, 'create.html', {'form': form})


#def create_cat(request):
#    if request.method == 'POST':
#        form = CategorieForm(request.POST)
#        if form.is_valid():
#            
#            categorie = form.save()
#            return redirect('cat_detail', categorie.id)
#        else:
#            print("*************************************")
#            print(form.errors)
#            print("*************************************")
#            form = CategorieForm()
#            return render(request, 'create_cat.html', {'form': form})  
#    else:
#        form = CategorieForm()
#        return render(request, 'create_cat.html', {'form': form})  


def all(request):
    categorie = Categorie.objects.all()
    product = Product.objects.all()
    return render(request, 'all.html',{'categorie':categorie,'product':product })
