from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup),
    path('login/', views.login_req),
]
