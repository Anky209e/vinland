
from django.shortcuts import render


def home(request):
    pcos_sum = """Polycystic ovary syndrome (PCOS) is a condition in which the ovaries produce an abnormal amount of androgens, male sex hormones that are usually present in women in small amounts."""
    skin_disease_sum ="""Acne, Eczema, Shingles(Herpes Zoster),Hives, Sunburn"""

    pcos_data = ["PCOS prediction",pcos_sum,"/models/pcos"]
    skin_data = ["Skin disease prediction",skin_disease_sum,"/models/skin_disease"]


    context={"models":[pcos_data,skin_data],"pagename":"Low body"}
    return render(request,"app_base.html",context)
# Create your views here.
