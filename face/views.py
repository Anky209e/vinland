from django.shortcuts import render

# Create your views here.
def home(request):
    park_sum = """Parkinson’s disease is a brain disorder that causes unintended or uncontrollable movements, such as shaking, stiffness, and difficulty with balance and coordination."""
    
    brain_sum = """A brain tumor is an abnormal growth or mass of cells in or around your brain. Brain tumors can be malignant (cancerous) or benign (noncancerous)."""
    
    cat_sum = """Cataract is a dense, cloudy area that forms in the lens of the eye. A cataract begins when proteins in the eye form clumps that prevent the lens from 
    sending clear images to the retina."""
    
    glaucoma_sum = """Glaucoma is a disease that damages your eye’s optic nerve. It usually happens when fluid builds up in the front part of your eye. That extra fluid increases the pressure in your eye, damaging the optic nerve."""
    
    park_data = ["Parkinson Disease",park_sum,"/models/parkinson","01"]
    brain_data = ["Brain Tumor",brain_sum,"/models/brain_tumor","02"]
    cat_data = ["Cataract Detection",cat_sum,"/models/eye_defect","03"]
    glaucoma_data = ["Glaucoma Detection",glaucoma_sum,"/models/galucoma","04"]

    context = {"models":[park_data,brain_data,cat_data,glaucoma_data],"pagename":"Head"}
    return  render(request,"app_base.html",context)