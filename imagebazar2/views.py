from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import *


def about(request):
    return render(request,"about.html")

def home(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {
        'images':images,
        'cats':cats
    }
    return render(request,"home.html",data)

def category(request,cid):
    cats = Category.objects.all()

    category = Category.objects.get(pk=cid) #it will give the particular category through cid
    print(category)




    images = Image.objects.filter(cat=category)
    data = {
        'images':images,
        'cats':cats
    }
    return render(request,"home.html",data)




def home_function(request):
    return redirect('/home')