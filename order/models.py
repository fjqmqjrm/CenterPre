from django.db import models


class Order(models.Model):
    # 유저 나중에 합칠 때
    # user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='주문시간')
    #cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE, default=None)
    #order_status = models.BooleanField(default=False) #주문상태
    def __str__(self): # 관리자 페이지에서 객체를 확인할때 속성값으로 받게되면 해당 값의 명이 출력. 아니면 이상한 `object`라는 명으로 출력됨
        return self.name

    class Meta: # 관리자 페이지 설정
        db_table = 'my_order' # DB에 저장될 테이블 이름 지정
        verbose_name = '주문'
        verbose_name_plural = '주문'
        # 복수형 지정안하면 "주문s"가 되는데요. s붙이지 않기 위해서.

