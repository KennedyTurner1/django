from django.urls import path, include

from .import views 

app_name = 'users'

urlpatterns = [
    path('',include('django.contrib.auth.urls')), #homepage/users
    path('register/',views.register, name='register'), #homepage/users/register
]