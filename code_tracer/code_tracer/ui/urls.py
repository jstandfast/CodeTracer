from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='ui/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]