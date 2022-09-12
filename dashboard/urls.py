from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.dash,name='dash'),
    path("", views.admin_product, name="admin_product"),
    path('', views.admin_categorie, name='admin_categorie'),
    path('', views.admin_details, name='admin_details'),
    path('', views.admin_cat_detail, name='admin_cat_detail'),
    path('', views.admin_all, name='admin_all'),   
    path('', views.admin_create, name='admin_create' ),
    path('', views.admin_create_cat, name='admin_create_cat'),


]



