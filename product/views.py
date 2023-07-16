from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm, EditForm
from django.contrib.auth import get_user


# Create your views here.
def product_list(request):
    '''product_list = Product.objects.all()
    return render(request, 'product/product.html', {'product_list': product_list})'''
    address_filter = request.GET.get('address', '')  # 주소 필터링 값을 가져옴

    if address_filter:  # 주소 필터링 값이 있다면 해당 주소의 게시글만 필터링
        product_list = Product.objects.filter(address=address_filter)
    else:  # 주소 필터링 값이 없다면 모든 게시글 표시
        product_list = Product.objects.filter()

    address_choices = Product.DISTRICT_CHOICES  # 주소 선택지

    context = {
        'product_list':  product_list,
        'address_choices': address_choices,
        'selected_address': address_filter,  # 선택한 주소를 템플릿으로 전달
    }
    return render(request, 'product/product.html', context)


def product_create(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)  # 파일을 처리하기 위해 request.FILES 전달

        if form.is_valid():
            form.save(request=request)
            return redirect('/product/')
    else:
        form = RegisterForm()
    return render(request, 'product/register_product.html', {'form': form})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})

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
    product.customer = request.user
    product.save()
    return redirect('product:product_list')

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():

            form.save()
            return redirect('/product/')
    else:
        form = EditForm(instance=product)

    return render(request, 'product/edit_product.html', {'form': form})