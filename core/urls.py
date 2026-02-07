from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/comments/', views.comments_api),
    path('api/comments/add/', views.comments_post_api),
]
