from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .models import CustomUser
from .forms import myUserCreationForm, UserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except:
            return HttpResponse("User not found")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse("Username or Password is not correct")
    
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = myUserCreationForm()
    if request.method == 'POST':
        form = myUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse("error occured")
    return render(request, 'register.html', {'form':form})

@login_required
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            redirect('home.html')
        else:
            return HttpResponse("Error occured")
    return render(request, 'update.html', {'form':form})

@login_required
def logoutUser(request):
    logout(request)
    return render(request, 'home.html')