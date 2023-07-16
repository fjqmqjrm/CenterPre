from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path('', views.community_view, name="community"),
    path("buy_review", views.buy_review, name="review"),
    path("free_board", views.freeboard_view, name="freeboard"),
    path('<int:pk>/', views.freeboard_list, name="freeboardDetail"),
    path('post/', views.freeboard_post, name="freeboardPost"),
    path('<int:pk>/edit/', views.freeboard_edit, name="freeboardEdit"),
]