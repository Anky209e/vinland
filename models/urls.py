from django.urls import path, include
from . import views

urlpatterns = [
    path('parkinson/',views.parkinson,name='parkinson'),
    path('heartattack/',views.heartattack,name='heartattack'),
    path('diabetes/',views.diabetes, name='diabetes'),
    path('pcos/',views.pcos, name='pcos')
]
