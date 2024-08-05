from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .models import *
# from .forms import OrderForm, CreateUserForm, CustomerForm
# from .filters import OrderFilter
# from .decorators import unauthenticated_user, allowed_users, admin_only
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
    products = Product.objects.all()
    men = Category.objects.get(name='Men')
    men_product = men.product_set.all()
    
    women = Category.objects.get(name='Women')
    women_product = women.product_set.all()
    
    watches = Category.objects.get(name='Watches')
    watches_product = watches.product_set.all()
    bags = Category.objects.get(name='Bags')
    bags_products = bags.product_set.all()
    shoes = Category.objects.get(name='Shoes')
    shoes_product = shoes.product_set.all()
    belts = Category.objects.get(name='Belts')
    belts_product = belts.product_set.all()
    caps = Category.objects.get(name='Caps')
    caps_product = caps.product_set.all()
    
    
    context = {'products': products, 
               'men_product': men_product, 
               'caps_product': caps_product,
               'women_product': women_product, 
               'watches_product': watches_product, 
               'bags_products': bags_products, 
               'shoes_product': shoes_product, 
               'belts_product': belts_product}
    return render(request, 'store/product.html', context)

def category_view(request, category_id=None):
    categories = Category.objects.all()
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=selected_category)
    else:
        selected_category = None
        products = Product.objects.all()

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'products': products
    }
    return render(request, 'store/product.html', context)

def blog(request):
    return render(request, 'store/blog.html')

def blog_details(request):
    return render(request, 'store/blog-detail.html')

def shopping_cart(request):
    return render(request, 'store/shoping-cart.html')


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'store/product-detail.html', context)

def product_detail(request):
    return render(request, 'store/product-detail.html')

def admin_page(request):
    return render(request, 'admin/admin_page.html')