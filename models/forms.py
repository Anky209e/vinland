from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
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
    

class MyUserCreationForm(UserCreationForm):
    class Meta:
        fields = []
