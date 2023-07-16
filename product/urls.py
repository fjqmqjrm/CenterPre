from django.urls import path, include
from . import views
from .views import product_delete, edit_product, product_create,product_list,product_detail

urlpatterns = [
    path('product/create/', product_create, name='product_post'),
    path('product/', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
    path('product/order/', views.order_list, name='order_list'),
    path('product/order/<int:pk>/', views.order_done, name='order_done'),
    path('product/<int:pk>/edit/', edit_product, name='product_edit'),
    ]