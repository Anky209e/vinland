from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('update/', views.updateUser, name='update'),
    path('logout/', views.logoutUser, name='logout')
]
