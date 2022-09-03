from django.shortcuts import render


def home(request):
    heart_sum="""heart summary"""
    diabetes_sum="""diabetes_sum"""
    maleria_sum="""maleria_sum"""
    pneumonia_sum="""pneumonia_sum"""

    heart_data=["Heart Attack",heart_sum,"/models/heartattack"]
    diabetes_data=["Diabetes prediction", diabetes_sum,"/models/diabetes"]
    maleria_data = ["Maleria prediction", maleria_sum,"/models/maleria"]
    pneumonia_data = ["Pneumonia prediction", pneumonia_sum, "/models/pneumonia"]


    context = {"models":[heart_data,diabetes_data,maleria_data,pneumonia_data],"pagename":"Blood"}
    return render(request, "app_base.html",context)



# Create your views here.