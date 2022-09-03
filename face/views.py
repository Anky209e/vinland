from django.shortcuts import render

# Create your views here.
def home(request):
    park_sum = """Summary for parkinson"""
    brain_sum = """Summary for brain tumor"""
    cat_sum = """Summary for Cataract"""
    glaucoma_sum = """Summary for galucoma"""
    
    park_data = ["Parkinson Disease",park_sum,"/models/parkinson"]
    brain_data = ["Brain Tumor",brain_sum,"/models/brain"]
    cat_data = ["Cataract Detection",cat_sum,"/models/cataract"]
    glaucoma_data = ["Glaucoma Detection",glaucoma_sum,"/models/galucoma"]

    context = {"models":[park_data,brain_data,cat_data,glaucoma_data]}
    return  render(request,"app_base.html",context)