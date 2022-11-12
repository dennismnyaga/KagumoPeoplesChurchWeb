from django.urls import path, include
from . import views


app_name = 'usersreg'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
]