from django.shortcuts import render
from django.http import HttpResponse, Http404

def homepage(request):
    return render(request, "home.html")

def aboutpage(request):
    return render(request, "about.html")


