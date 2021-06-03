from django.urls import path
from .views import StudentLogin, StudentRegistration

urlpatterns = [
    path('studentlogin/', StudentLogin, name='StudentLogin'),
    path('studentregistration/', StudentRegistration, name='StudentRegistration'),
]
