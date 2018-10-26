from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Form, Question, Ans
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def homepage(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'Forms/homepage.htm', context)
    return redirect('login')
'''
def error404(request):
    context = {}
    return render(request, 'Forms/index.htm', context)
'''

def createForm(request):
    context = {}
    return render(request, 'Forms/createForm.htm', context)
            