from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserRegisterView


app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page="logout.html"), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
