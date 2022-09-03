from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home),
    path('parkinson/',views.parkinson,name='parkinson'),
    path('heartattack/',views.heartattack,name='heartattack'),
    path('diabetes/',views.diabetes, name='diabetes'),
    path('pcos/',views.pcos, name='pcos')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
