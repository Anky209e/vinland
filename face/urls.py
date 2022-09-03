from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.home,name="head_home")
    
]
