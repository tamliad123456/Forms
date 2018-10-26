from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Form, Question, Ans
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'Forms/homepage.htm', context)
    return redirect('login')

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                return redirect('../homepage/')
            else:
                return render(request, 'Forms/login.htm', {'form' : form})
        else:
            form = AuthenticationForm()
            return render(request, 'Forms/login.htm', {'form' : form})
    else:
        return redirect('../homepage/')


def error404(request):
    context = {}
    return render(request, 'Forms/index.html', context)
            