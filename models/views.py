from django.shortcuts import render
from .forms import ParkkinsonForm
from .classes.parkinson_detect import predict_parkinson

def home(request):
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

# Create your views here.
