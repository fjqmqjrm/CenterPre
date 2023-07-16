from django.db import models
from users.models import User

class Product(models.Model):
    product_name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품 상세설명')
    product_image = models.FileField(upload_to='images/', verbose_name='상품 이미지', null=True, default=None)
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    order_status = models.BooleanField(default=False, verbose_name='주문상태') #주문상태
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'my_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'
# Create your models here.
