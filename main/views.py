from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def new_deal(request):
    return render(request, 'main/new_deal.html')

def one(request):
    return render(request, 'main/one.html')