from django.db import models



class CartItem(models.Model):
    # user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '장바구니'
        verbose_name_plural = f'{verbose_name} 목록' #복수형 이름 지정
        ordering = ['-pk'] #생성일시의 역순(최신순) 정렬
    #해당 장바구니 아이템을 문자열로 표현하기 위한 메서드
    def __str__(self):
        return self.product.product_name
