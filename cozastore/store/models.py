from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="mypic2.jpeg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name or "Unknown"

class Banner(models.Model):
    name = models.CharField(max_length=260)
    image = models.ImageField()
    title = models.CharField(max_length=260)
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    name = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField(blank=True)
    STATUS_CHOICES = [
    ('large', 'Large'),
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('xl', 'XL'),
    ('xxl', 'XXL'),
    ('xxxl', 'XXXL'),
    ]
    size = models.CharField(max_length=10, choices=STATUS_CHOICES)
    STATUS_CHOICES = [
    ('red', 'Red'),
    ('yellow', 'Yellow'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('orange', 'Orange'),
    ('purple', 'Purple'),
    ('black', 'Black'),
    ('white', 'White'),
    ]
    color = models.CharField(max_length=10, choices=STATUS_CHOICES)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
    

class Cart(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    price = models.FloatField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    total = models.FloatField()
    
class Blog(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(default="mypic2.jpeg", null=True, blank=True)
    author = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=250)
    content1 = models.TextField(blank=True, null=True)
    content2 = models.TextField(blank=True, null=True)
    featured_product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    
class Comment(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200, null=True)
    website = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    
class Social(models.Model):
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)
    image7 = models.ImageField(null=True, blank=True)
    image8 = models.ImageField(null=True, blank=True)
    image9 = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=250, null=True, blank=True)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS) 
    note = models.CharField(max_length=1000, null=True) 
    
    def __str__(self):
        return self.product.name