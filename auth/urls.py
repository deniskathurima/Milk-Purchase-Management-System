from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as denis_views

urlpatterns = [
    path('sign_up', denis_views.sign_up, name="signup-url"),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login-url'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout-url'),
]
