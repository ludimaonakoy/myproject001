from django.shortcuts import render
from django.http import HttpResponse
from .models import blog

def home(request):
    blogs = blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})
# Create your views here.
