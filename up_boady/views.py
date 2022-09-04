from django.shortcuts import render

# Create your views here.
def home(request):
    heart_sum = """"""
    lung_cancer_sum = """Summary for Lung Cancer"""
    
    skin_sum = """Summary for S"""
    covid_sum = """Summary for COVID"""
    pneumonia_sum = """Summary for pneumonia"""
    liver_sum = """Summary for Liver Patient"""

    
    heart_data = ["Heart Attack",heart_sum,"/models/heartattack"]
    lung_data = ["Lung Cancer",lung_cancer_sum,"/models/lung_cancer"]
    
    skin_data = ["Skin Disease",skin_sum,"/models/skin_disease"]
    covid_data = ["COVID",covid_sum,"/models/covid19"]
    pneu_data = ["Pneumonia Detection",pneumonia_sum,"/models/pneumonia"]
    liver_data = ["Liver Patient",liver_sum,"/models/liver_defect"]



    context = {"models":[heart_data,lung_data,skin_data,covid_data,pneu_data,liver_data]}
    return  render(request,"app_base.html",context)