from dataclasses import fields
from django import forms
class ParkkinsonForm(forms.Form):
    MDVP_FO = forms.FloatField()
    MDVP_fhi = forms.FloatField()
    MDVP_lo = forms.FloatField()
    MDVP_jitter = forms.FloatField()
    MDVP_jitter_abs = forms.FloatField()
    
        