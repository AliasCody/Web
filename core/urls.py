from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # ← 首頁
    path('api/comments/', views.comments_api),      # ← GET
    path('api/comments/add/', views.comments_post_api),  # ← POST
]
