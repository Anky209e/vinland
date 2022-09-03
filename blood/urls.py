from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='blood_home')
]
