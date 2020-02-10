from django.contrib import admin
from django.urls import path
from . import views
from users.views import verify

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/list/', views.PostListView.as_view(), name='blog-list'),
    path('about/', views.about, name='blog-about'),
    path('register/verify/<uuid>', verify, name='blog-verify'),
]