from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['title', 'image', 'description', 'price', 'date']
    search_fields = ['title', 'description']

admin.site.register(Product, ProductAdmin)
