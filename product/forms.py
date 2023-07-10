from django import forms
from .models import Product

class RegisterForm(forms.Form):
    product_name = forms.CharField(max_length=64, label='상품명')
    price = forms.IntegerField(label='상품가격')
    description = forms.CharField(label='상품설명')
    product_image = forms.FileField(label='상품이미지')

    def save(self, request):
        product_name = self.cleaned_data['product_name']
        price = self.cleaned_data['price']
        description = self.cleaned_data['description']
        product_image = request.FILES['product_image']  # 이미지 파일 가져오기

        product = Product(
            product_name=product_name,
            price=price,
            description=description
        )
        product.product_image.save(product_image.name, product_image)  # 이미지 파일 저장
        product.save()