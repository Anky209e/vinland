from django.urls import path, include
from . import views

urlpatterns = [
    path('parkinson/',views.home,name='parkinson')
]
