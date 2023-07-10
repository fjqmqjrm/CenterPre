from django.shortcuts import render, redirect
from .forms import OrderForm
from product.models import Product


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product']
            product = Product.objects.get(pk=product_id)
            order = product.order_set.create()  # 주문 생성
            # 필요한 주문 정보를 설정
            product.order_status = True
            product.save()
            order.save()
            return redirect('product:product')  # 주문 완료 페이지로 리다이렉트
    else:
        form = OrderForm()

    return render(request, 'product/product.html', {'form': form})