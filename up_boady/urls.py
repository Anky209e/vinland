from django.urls import path, include
from . import views
urlpatterns = [
    
    path('',views.home,name="up_body_home")
    
]
