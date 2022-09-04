from django.shortcuts import render


def home(request):
    heart_sum="""A heart attack occurs when the flow of blood to the heart is severely reduced or blocked."""
    diabetes_sum="""Diabetes is a metabolic disease that causes high blood sugar."""
    maleria_sum="""Malaria is a life-threatening disease caused by parasites that are transmitted to people through the bites of infected female Anopheles mosquitoes."""
    pneumonia_sum="""Pneumonia is a form of acute respiratory infection that affects the lungs."""

    heart_data=["Heart Attack",heart_sum,"/models/heartattack"]
    diabetes_data=["Diabetes prediction", diabetes_sum,"/models/diabetes"]
    maleria_data = ["Maleria prediction", maleria_sum,"/models/maleria"]
    pneumonia_data = ["Pneumonia prediction", pneumonia_sum, "/models/pneumonia"]


    context = {"models":[heart_data,diabetes_data,maleria_data,pneumonia_data],"pagename":"Blood"}
    return render(request, "app_base.html",context)



# Create your views here.