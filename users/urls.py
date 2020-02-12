from django.urls import path
from .views import verify, register
from django.contrib.auth import views

urlpatterns = [
    path('verify/<uuid>/', verify, name='users-verify'),
    path('register/', register, name='users-register'),
    path('login/', views.LoginView.as_view(template_name="users/login.html"), name='users-login'),
    path('logout/', views.LogoutView.as_view(template_name="users/logout.html"), name='users-logout'),
]