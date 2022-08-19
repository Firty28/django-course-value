from django.urls import path
from user.views import login, register, home, profile
from django.contrib.auth.views import LogoutView, LoginView
from .forms import LoginForm

app_name = 'user'

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='user/login.html', next_page='/', authentication_form=LoginForm), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
