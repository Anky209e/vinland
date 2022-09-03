from django.shortcuts import render

from .classes.heart_attack_detection import predict_heartattack
from .forms import ParkkinsonForm, HeartattackForm
from .classes.parkinson_detect import predict_parkinson

def parkinson(request):
    if request.method == 'POST':
        form = ParkkinsonForm(request.POST)
        if form.is_valid():
            MDVP_FO = form.cleaned_data['MDVP_FO']
            MDVP_fhi = form.cleaned_data['MDVP_fhi']
            MDVP_lo = form.cleaned_data['MDVP_lo']
            MDVP_jitter = form.cleaned_data['MDVP_jitter']
            MDVP_jitter_abs = form.cleaned_data['MDVP_jitter_abs']
            params = [MDVP_FO, MDVP_fhi, MDVP_lo, MDVP_jitter, MDVP_jitter_abs]
            res = predict_parkinson(params)
            print(res)
            acc = res['acc']
            result = res['result']
            cures = res['cures']

            context = {'form':form,
                        'acc':acc,
                        'result':result,
                        'cures':cures}
    else:
        form = ParkkinsonForm()
        context = {'form':form}
    return render(request, 'parkkinson.html', context=context)


def heartattack(request):
    if request.method == 'POST':
        form = HeartattackForm(request.POST)
        if form.is_valid():
            age= form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            chest_pain_type = form.cleaned_data['chest_pain_type']
            trtbps = form.cleaned_data['trtbps']
            cholestrol = form.cleaned_data['cholestrol']
            params = [age, sex, chest_pain_type,trtbps,cholestrol]
            res = predict_heartattack(params)
            print(res)
            acc = res['acc']
            result = res['result']
            cures = res['cures']

            context = {'form':form,
                        'acc':acc,
                        'result':result,
                        'cures':cures}
    else:
        form = HeartattackForm()
        context = {'form':form}
    return render(request, 'heartattack.html', context=context)

# Create your views here.
