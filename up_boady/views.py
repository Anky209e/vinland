from django.shortcuts import render

# Create your views here.
def home(request):
    heart_sum = """A heart attack occurs when the flow of blood to the heart is severely reduced or blocked"""
    lung_cancer_sum = """Lung cancer is cancer that forms in tissues of the lung, usually in the cells that line the air passages."""
    
    skin_sum = """Acne, Eczema, Shingles(Herpes Zoster),Hives, Sunburn"""
    covid_sum = """COVID-19  causes lung complications such as pneumonia and, in the most severe cases, acute respiratory distress syndrome, or ARDS."""
    pneumonia_sum = """Pneumonia is a form of acute respiratory infection that affects the lungs"""
    liver_sum = """Detects any type of liver infection and unsual behaviour"""

    
    heart_data = ["Heart Attack",heart_sum,"/models/heartattack"]
    lung_data = ["Lung Cancer",lung_cancer_sum,"/models/lung_cancer"]
    
    skin_data = ["Skin Disease",skin_sum,"/models/skin_disease"]
    covid_data = ["COVID",covid_sum,"/models/covid19"]
    pneu_data = ["Pneumonia Detection",pneumonia_sum,"/models/pneumonia"]
    liver_data = ["Liver Patient",liver_sum,"/models/liver_defect"]



    context = {"models":[heart_data,lung_data,skin_data,covid_data,pneu_data,liver_data]}
    return  render(request,"app_base.html",context)