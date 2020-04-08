from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def index(request):
	return render(request,'index.html')

def dadar(request):
	return render(request,'dadar.html')

def borivali(request):
	return render(request,'borivali.html')

def chembur(request):
	return render(request,'chembur.html')

