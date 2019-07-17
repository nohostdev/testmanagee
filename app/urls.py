from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from . import views as user_views

urlpatterns = [
    path('',user_views.home,name='index'),
    path('register/', user_views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]