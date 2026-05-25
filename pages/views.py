from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'pages/home.html')

def products_view(request):
    return render(request, 'pages/products.html')