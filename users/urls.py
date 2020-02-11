from django.urls import path
from .views import verify, register

urlpatterns = [
    path('verify/<uuid>/', verify, name='blog-verify'),
    path('register/', register, name='blog-register'),
]