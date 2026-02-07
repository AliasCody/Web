from django.urls import path
from . import views

urlpatterns = [
    path("api/comments/", views.comments_api),
]
