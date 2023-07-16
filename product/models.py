from django.db import models
from users.models import User

class Product(models.Model):
    DISTRICT_CHOICES = (
        ('강남구', '강남구'),
        ('강동구', '강동구'),
        ('강북구', '강북구'),
        ('강서구', '강서구'),
        ('관악구', '관악구'),
        ('광진구', '광진구'),
        ('구로구', '구로구'),
        ('금천구', '금천구'),
        ('노원구', '노원구'),
        ('도봉구', '도봉구'),
        ('동대문구', '동대문구'),
        ('동작구', '동작구'),
        ('마포구', '마포구'),
        ('서대문구', '서대문구'),
        ('서초구', '서초구'),
        ('성동구', '성동구'),
        ('성북구', '성북구'),
        ('송파구', '송파구'),
        ('양천구', '양천구'),
        ('영등포구', '영등포구'),
        ('용산구', '용산구'),
        ('은평구', '은평구'),
        ('종로구', '종로구'),
        ('중구', '중구'),
        ('중랑구', '중랑구'),
    )
    address = models.CharField(max_length=50, choices=DISTRICT_CHOICES,null=True)
    detail_address = models.CharField(max_length=50,null=True)
    product_name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품 상세설명')
    product_image = models.FileField(upload_to='images/', verbose_name='상품 이미지', null=True, default=None)
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    order_status = models.BooleanField(default=False, verbose_name='주문상태') #주문상태
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='구매자')
    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'my_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'
# Create your models here.
