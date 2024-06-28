from django.contrib import admin
from .models import CartItem
from django.http import HttpResponse
import csv

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
        readonly_fields = ('user', 'product', 'quantity')
