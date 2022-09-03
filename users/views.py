import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import SignupForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignupForm()

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username= user.username, password = raw_password)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form':form})