from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.home),
    path('login/', 
        LoginView.as_view(template_name='accounts/login.html'), 
        name="login"),
    path('logout/', 
        LogoutView.as_view(template_name='accounts/logout.html'), 
        name="logout"),
    path('signup/',views.signup,name = "signup"),
]