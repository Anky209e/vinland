from django.shortcuts import render
from .forms import ImageForm
from .classes.heart_attack_detection import predict_heartattack
from .forms import ParkkinsonForm, HeartattackForm,DiabetesForm,PcosForm
from .classes.parkinson_detect import predict_parkinson
from .classes.pcos_detection import predict_pcos
from .classes.diabetes_predict import predict_diabetes



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


def home(request):

    return render(request,"model_home.html")
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

def diabetes(request):
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            pregnancies= form.cleaned_data['pregnancies']
            glucose= form.cleaned_data['glucose']
            bloodpressure = form.cleaned_data['bloodpressure']
            skin_thickness = form.cleaned_data['skin_thickness']
            insulin = form.cleaned_data['insulin']
            bmi = form.cleaned_data['bmi']
            diabetes_pedigree_function=form.cleaned_data['diabetes_pedigree_function']
            age = form.cleaned_data['age']

            params = [pregnancies, glucose, bloodpressure, skin_thickness, insulin,bmi,diabetes_pedigree_function, age]
            res = predict_diabetes(params)
            print(res)
            acc = res['acc']
            result = res['result']
            cures = res['cures']

            context = {'form':form,
                        'acc':acc,
                        'result':result,
                        'cures':cures}
    else:
        form = DiabetesForm()
        context = {'form':form}
    return render(request, 'diabetes.html', context=context)

def pcos(request):
    if request.method == 'POST':
        form = PcosForm(request.POST)
        if form.is_valid():
            beta_1_hcg_mIU_mL= form.cleaned_data['beta_1_hcg_mIU_mL']
            beta_2_hcg_mIU_mL= form.cleaned_data['beta_2_hcg_mIU_mL']
            amh_ng_mL= form.cleaned_data['amh_ng_mL']
            params = [beta_1_hcg_mIU_mL,beta_2_hcg_mIU_mL,amh_ng_mL]
            res = predict_pcos(params)
            print(res)
            acc = res['acc']
            result = res['result']
            cures = res['cures']

            context = {'form':form,
                        'acc':acc,
                        'result':result,
                        'cures':cures}
    else:
        form = PcosForm()
        context = {'form':form}
    return render(request, 'pcos.html', context=context)


def maleria(request):
    name = "Maleria"
    html_path = "cnn/maleria.html"

    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/model_images/" + str(request.FILES["image_field"]).replace(" ", "_")
        
        from .classes.maleria import predict_maleria
        result = predict_maleria(img_path)


        return render(request, "image_base.html", {"image_form": None, "name":name, "list":result})
    else:
        image_form = ImageForm()

        return render(request, "image_base.html", {"image_form": image_form, "name":name})

def pneumonia(request):
    name = "Pneumonia"
    html_path = "cnn/pneumonia.html"

    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/model_images/" + str(request.FILES["image_field"]).replace(" ", "_")
        
        from .classes.pneumonia_detect import predict
        result = predict(img_path)


        return render(request, "image_base.html", {"image_form": None, "name":name, "list":result})
    else:
        image_form = ImageForm()

        return render(request, "image_base.html", {"image_form": image_form, "name":name})



def brain_tumor(request):
    name = "Brain Tumor"
    html_path = "cnn/brain_tumor.html"

    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/model_images/" + str(request.FILES["image_field"]).replace(" ", "_")
        
        from .classes.tumor_detect import check_tumor
        result = check_tumor(img_path)


        return render(request, "image_base.html", {"image_form": None, "name":name, "list":result})
    else:
        image_form = ImageForm()

        return render(request, "image_base.html", {"image_form": image_form, "name":name})

def covid19(request):
    name = "Covid19"
    html_path = "cnn/pneumonia.html"

    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/model_images/" + str(request.FILES["image_field"]).replace(" ", "_")
        
        from .classes.covid_detect import predict
        result = predict(img_path)


        return render(request, "image_base.html", {"image_form": None, "name":name, "list":result})
    else:
        image_form = ImageForm()

        return render(request, "image_base.html", {"image_form": image_form, "name":name})


def skin_disease(request):
    name = "Skin disease"
    html_path = "cnn/skin_disease.html"

    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/model_images/" + str(request.FILES["image_field"]).replace(" ", "_")
        
        from .classes.skin_disease import predict
        result = predict(img_path)


        return render(request, "image_base.html", {"image_form": None, "name":name, "list":result})
    else:
        image_form = ImageForm()

        return render(request, "image_base.html", {"image_form": image_form, "name":name})