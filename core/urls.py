from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#---------------------------------

urlpatterns = [

    path("", views.home, name='home'),
    path("contact", views.contact, name='contact'),
    path("product", views.product, name="product"),
    path('categorie', views.categorie, name='categorie'),
    path('details/<int:id>/', views.details, name='details'),
    path('cat_detail/<int:id>/', views.cat_detail, name='cat_detail'),
    path('confirm', views.confirm, name='confirm'),
    #path('product/create/', views.create, name='create' ),
    #path('categorie/create/', views.create_cat, name='create_cat'),
    path('all/', views.all, name='all'),
    path('dash/',include('dashboard.urls')),


   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    urlpatterns += staticfiles_urlpatterns()







