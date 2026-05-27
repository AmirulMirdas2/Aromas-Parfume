# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import products

admin.site.register(products)