from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request,'appk/home.html')
def userlogin(request):
    return render(request,'appk/login.html')
def register(request):
    return render(request,'appk/register.html')