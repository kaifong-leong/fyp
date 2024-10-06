from django.urls import path
from . import views # . because it is in the same directory

urlpatterns = [
    
    path('', views.homepage, name=""), 
    path('register', views.register, name="register"), # preference to keep name parameter same as route name
    path('my-login', views.my_login, name="my-login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user-logout', views.user_logout, name="user-logout"),
]