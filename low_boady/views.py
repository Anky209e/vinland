
from django.shortcuts import render


def home(request):
    pcos_sum = """pcos_summ"""
    skin_disease_sum ="""skin_disease_sum"""

    pcos_data = ["PCOS prediction",pcos_sum,"/models/pcos"]
    skin_data = ["Skin disease prediction",skin_disease_sum,"/models/skin_disease"]


    context={"models":[pcos_data,skin_data],"pagename":"Low body"}
    return render(request,"app_base.html",context)
# Create your views here.
