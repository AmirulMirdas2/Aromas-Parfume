# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect, get_object_or_404
# pyrefly: ignore [missing-import]
from django.http import HttpResponse
# pyrefly: ignore [missing-import]
from django.contrib.auth import authenticate, login, logout
# pyrefly: ignore [missing-import]
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# pyrefly: ignore [missing-import]
from django.contrib.auth.decorators import login_required
from .models import products, Cart, CartItem

# Create your views here.

def home_view(request):
    return render(request, 'pages/home.html')

def products_view(request):
    all_products = products.objects.all()
    return render(request, 'pages/products.html', {'products': all_products})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url if next_url else 'home')
    else:
        form = AuthenticationForm(request)
    return render(request, 'pages/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url if next_url else 'home')
    else:
        form = UserCreationForm()
    return render(request, 'pages/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total_price = sum(item.total_price for item in items)
    return render(request, 'pages/cart.html', {'cart': cart, 'items': items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(products, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('cart')