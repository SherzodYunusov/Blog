from django.shortcuts import render, redirect
from .models import *

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def blog(request):
    content = {
        "blog": Maqola.objects.get(id=1),
        "blog2": Maqola.objects.get(id=2),
        "blog3": Maqola.objects.get(id=3),

    }
    return render(request, 'blog.html', content)


def maqola1(request):

    content = {
        "maqola1": Maqola.objects.get(id=1),
    }
    return render(request, 'maqola.html', content)

def maqola2(request):

    content = {
        "maqola2": Maqola.objects.get(id=2),
    }
    return render(request, 'maqola2.html', content)

def maqola3(request):

    content = {
        "maqola3": Maqola.objects.get(id=3),
    }
    return render(request, 'maqola3.html', content)

# Create your views here.
