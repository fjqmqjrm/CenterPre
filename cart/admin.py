from django.contrib import admin
from cart.models import CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('product',)
# Register your models here.

admin.site.register(CartItem, CartAdmin)
