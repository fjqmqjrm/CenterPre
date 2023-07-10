
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product_list'


class ProductCreate(FormView):

    template_name = 'product/register_product.html'#폼을 렌더링할 경로
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        form.save(request=self.request)  # RegisterForm의 save 메서드 호출
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'product/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('/product/')
def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('product_list')

def order_list(request): #책이랑 다르게 작성함
    dones = Product.objects.filter(order_status=True)
    return render(request, 'product/order_list.html', {'dones': dones})

def order_done(request, pk):
    product = Product.objects.get(id=pk)
    product.order_status = True
    product.save()
    return redirect('product_list')