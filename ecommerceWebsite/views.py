from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'Home.html')

def school(request):
    return render(request,'school.html')

def electronic(request):
    return render(request,'electronics.html')

def fashion(request):
    return render(request,'fashion.html')

def footwear(request):
    return render(request,'footwear.html')

def laptops(request):
    return render(request,'laptopes.html')

def mobiles(request):
    return render(request,'mobiles.html')