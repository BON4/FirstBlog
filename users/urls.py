from django.urls import path
from .views import verify

urlpatterns = [
    path('verify/<uuid>/', verify, name='blog-verify'),
]