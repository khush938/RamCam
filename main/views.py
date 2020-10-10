from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from . forms import RegistrationForm
from. models import CityName, AreaName
import time

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')

        return render(request, 'main/logfinal.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

@staff_member_required
def register(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            form = RegistrationForm

            if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    messages.success(request, f"New account created: {username}")
            context = {'form':form}
            return render(request, 'main/registerfinal.html', context )
        else:
            return redirect('home')
    else:
        return redirect('home')

@login_required(login_url='login')
def homepage(request):
    city_names = CityName.objects.all()
    context = {'cities':city_names}
    return render(request, 'main/index.html', context)

@login_required(login_url='login')
def video_feed(request, city_name, area_name):
    context = {'city':city_name, 'area':area_name}
    return render(request, 'main/sardard.html', context)

@login_required(login_url='login')
def homepage_with_areas(request, city_name):
    area_names = AreaName.objects.filter(city_name__city_name=city_name) 
    context = {'city':city_name, 'areas':area_names}
    return render(request, 'main/index_with_area.html', context)