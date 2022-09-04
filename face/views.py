from django.shortcuts import render

# Create your views here.
def home(request):
    park_sum = """Parkinson’s disease is a brain disorder that causes unintended or uncontrollable movements, such as shaking, stiffness, and difficulty with balance and coordination."""
    
    brain_sum = """A brain tumor is an abnormal growth or mass of cells in or around your brain."""
    
    cat_sum = """Summary for Cataract"""
    glaucoma_sum = """Summary for galucoma"""
    
    park_data = ["Parkinson Disease",park_sum,"/models/parkinson","01"]
    brain_data = ["Brain Tumor",brain_sum,"/models/brain_tumor","02"]
    cat_data = ["Cataract Detection",cat_sum,"/models/eye_defect","03"]
    glaucoma_data = ["Glaucoma Detection",glaucoma_sum,"/models/galucoma","04"]

    context = {"models":[park_data,brain_data,cat_data,glaucoma_data],"pagename":"Head"}
    return  render(request,"app_base.html",context)