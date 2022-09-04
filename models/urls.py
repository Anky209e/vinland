from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home),
    path('parkinson/',views.parkinson,name='parkinson'),
    path('heartattack/',views.heartattack,name='heartattack'),
    path('diabetes/',views.diabetes, name='diabetes'),
    path('pcos/',views.pcos, name='pcos'),
    path('maleria/',views.maleria, name='maleria'),
    path('pneumonia/',views.pneumonia, name='pneumonia'),
    path('brain_tumor/', views.brain_tumor, name='brain_tumor'),
    path('covid19/',views.covid19,name='covid19'),
    path('skin_disease/',views.skin_disease, name="skin_disease"),
    path('eye_defect/',views.eye_defect, name='eye_defect'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
