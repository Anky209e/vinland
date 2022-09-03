from django.shortcuts import render

# Create your views here.
def home(request):
    heart_sum = """Summary for Heart Attack"""
    lung_cancer_sum = """Summary for Lung Cancer"""
    brest_sum = """Summary for Breast Cancer"""
    skin_sum = """Summary for Skin Disease"""
    covid_sum = """Summary for COVID"""
    pneumonia_sum = """Summary for pneumonia"""
    liver_sum = """Summary for Liver Patient"""

    
    heart_data = ["Heart Attack",heart_sum,"/models/heartattack"]
    brain_data = ["Lung Cancer",lung_cancer_sum,"/models/lung"]
    brest_data = ["Breast Cancer",brest_sum,"/models/brest_cancer"]
    skin_data = ["Skin Disease",skin_sum,"/models/skin"]
    covid_data = ["COVID",covid_sum,"/models/covid"]
    pneu_data = ["Pneumonia Detection",pneumonia_sum,"/models/pneumonia"]
    liver_data = ["Liver Patient",liver_sum,"/models/liver"]



    context = {"models":[heart_data,brain_data,brest_data,skin_data,covid_data,pneu_data,liver_data]}
    return  render(request,"app_base.html",context)