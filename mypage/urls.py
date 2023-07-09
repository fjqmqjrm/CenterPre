from django.urls import path
from . import views

app_name = "mypage"

urlpatterns = [
    path('', views.mypage_view, name="mypage"),
    path("edit", views.edit_view, name="edit"),
]