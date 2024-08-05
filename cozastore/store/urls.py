from django.urls import path
from django.contrib import admin
#from .views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Correct root path
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('product/', views.category_view, name='product'),  # Use category_view for product page
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),  # Updated URL pattern
    path('product_detail/', views.product_detail, name='product_detail'),  # Updated URL pattern
    path('admin_page/', views.admin_page, name='admin_page'),
    path('category/<int:category_id>/', views.category_view, name='category_products'),  # Category filter path
]