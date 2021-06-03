from django.contrib.auth import logout
from django.urls import path
from .views import StaffLogin, StaffRegister, Logout

urlpatterns = [
    path('stafflogin/', StaffLogin, name='stafflogin'),
    path('staffregister/', StaffRegister, name='staffregister'),
    path('logout/', Logout, name='logout')  
]
