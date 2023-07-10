from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product',)

#admin.site.register() 함수를 사용하여 Order 모델과 OrderAdmin 클래스를 관리자 사이트에 등록
admin.site.register(Order, OrderAdmin)
# Register your models here.
