from django.contrib import admin
from . import models
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Brand)
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Social)
admin.site.register(Size)