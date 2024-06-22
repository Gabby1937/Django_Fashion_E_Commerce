from django.urls import path
from django.contrib import admin
#from .views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Correct root path
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('product_details/', views.product_details, name='product_details'),
]