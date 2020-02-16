from django.urls import path
from .views import verify, register
from django.contrib.auth import views
from . import views as user_views
from .forms import UserAuthenticationForm

urlpatterns = [
    path('verify/<uuid>/', verify, name='users-verify'),
    path('profile/', user_views.profile_view, name='users-profile'),
    path('register/', register, name='users-register'),
    path('login/', views.LoginView.as_view(template_name="users/login.html", authentication_form=UserAuthenticationForm), name='users-login'),
    path('logout/', views.LogoutView.as_view(template_name="users/logout.html"), name='users-logout'),
    path('<int:id>/liked_posts/', user_views.UserLikedPostsView.as_view(), name='users-likes'),
    path('<int:id>/disliked_posts/', user_views.UserDisLikedPostsView.as_view(), name='users-dislikes'),
]