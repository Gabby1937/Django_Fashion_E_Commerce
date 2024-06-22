from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'store/home-02.html')

def index(request):
    return render(request, 'store/home-03.html')

def contact(request):
    return render(request, 'store/contact.html')

def about(request):
    return render(request, 'store/about.html')

def product(request):
    return render(request, 'store/product.html')

def blog(request):
    return render(request, 'store/blog.html')

def blog_details(request):
    return render(request, 'store/blog-detail.html')

def shopping_cart(request):
    return render(request, 'store/shoping-cart.html')

def product_details(request):
    return render(request, 'store/product-detail.html')
