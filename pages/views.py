# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.http import HttpResponse
from .models import products

# Create your views here.

def home_view(request):
    return render(request, 'pages/home.html')

def products_view(request):
    all_products = products.objects.all()
    return render(request, 'pages/products.html', {'products': all_products})