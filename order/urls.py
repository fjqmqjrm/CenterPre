from django.urls import path
from . import views
from .views import create_order
app_name = 'order'

urlpatterns = [
    path('product/order/', create_order, name='order_create'),

    ]