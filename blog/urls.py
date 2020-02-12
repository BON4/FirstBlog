from django.contrib import admin
from django.urls import path
from . import views
from users.views import verify

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/list/', views.PostListView.as_view(), name='blog-list'),
    path('about/', views.about, name='blog-about'),
    path('post/like/<int:pk>/', views.PostLikeView.as_view(), name='blog-post-like'),
    path('post/dislike/<int:pk>/', views.PostDisLikeView.as_view(), name='blog-post-dislike'),
]