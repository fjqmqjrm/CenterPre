from django.urls import path, include
from . import views
from .views import ProductCreate, ProductList, ProductDetail, product_delete

urlpatterns = [
    path('product/create/', ProductCreate.as_view()),
    path('product/', ProductList.as_view(),name='product_list'),
    path('product/<int:pk>/', ProductDetail.as_view(),name='product_detail'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
    path('product/order/', views.order_list, name='order_list'),
    path('product/order/<int:pk>/', views.order_done, name='order_done')
    ]