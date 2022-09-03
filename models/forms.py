from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import ImageModel

class ParkkinsonForm(forms.Form):
    MDVP_FO = forms.FloatField()
    MDVP_fhi = forms.FloatField()
    MDVP_lo = forms.FloatField()
    MDVP_jitter = forms.FloatField()
    MDVP_jitter_abs = forms.FloatField()


class HeartattackForm(forms.Form):
    sex = forms.CharField(max_length=10)
    chest_pain_type = forms.CharField(max_length=50)
    age= forms.IntegerField(validators=[MaxValueValidator(120)])
    trtbps = forms.FloatField()
    cholestrol = forms.FloatField()
    
class DiabetesForm(forms.Form):
    pregnancies = forms.IntegerField()
    glucose = forms.IntegerField()
    bloodpressure = forms.IntegerField()
    skin_thickness = forms.IntegerField()
    insulin= forms.IntegerField()
    bmi = forms.IntegerField()
    diabetes_pedigree_function  = forms.IntegerField()
    age = forms.IntegerField()


class PcosForm(forms.Form):
    beta_1_hcg_mIU_mL = forms.FloatField()
    beta_2_hcg_mIU_mL = forms.FloatField()
    amh_ng_mL = forms.FloatField()




class MyUserCreationForm(UserCreationForm):
    class Meta:
        fields = []



class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = ["image_field"]