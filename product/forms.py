from django import forms
from .models import Product
from django.contrib.auth import get_user

class RegisterForm(forms.Form):
    product_name = forms.CharField(max_length=64, label='상품명')
    price = forms.IntegerField(label='상품가격')
    description = forms.CharField(label='상품설명')
    product_image = forms.FileField(label='상품이미지')
    address = forms.ChoiceField(label='구', choices=Product.DISTRICT_CHOICES)
    detail_address = forms.CharField(label='상세주소')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'class': 'form-select'})
    def save(self, request):
        product_name = self.cleaned_data['product_name']
        price = self.cleaned_data['price']
        description = self.cleaned_data['description']
        product_image = request.FILES['product_image']  # 이미지 파일 가져오기
        author = request.user
        address = self.cleaned_data['address']

        product = Product(
            product_name=product_name,
            price=price,
            description=description,
            author=author,
            address=address,
        )
        product.product_image.save(product_image.name, product_image)  # 이미지 파일 저장
        product.save()


class EditForm(forms.ModelForm):
    product_name = forms.CharField(max_length=64, label='상품명')
    price = forms.IntegerField(label='상품가격')
    description = forms.CharField(label='상품설명')
    product_image = forms.FileField(label='상품이미지')
    class Meta:
        model = Product
        fields = ('product_name','price','description','product_image')