from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
#from core import *

urlpatterns = [
    path('',views.dash,name='dash'),
    path('admin_product', views.admin_product, name='admin_product'),
    path('admin_categorie', views.admin_categorie, name='admin_categorie'),
    path('admin_details/<int:id>/', views.admin_details, name='admin_details'),
    path('admin_cat_detail/<int:id>/', views.admin_cat_detail, name='admin_cat_detail'),
    path('admin_all', views.admin_all, name='admin_all'),   
    path('admin_product/admin_create', views.admin_create, name='admin_create' ),
    path('admin_categorie/sadmin_create_cat', views.admin_create_cat, name='admin_create_cat'),


]



