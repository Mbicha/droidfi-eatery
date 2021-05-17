from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meal
from .forms import *

# Create your views here.
def index(request):
    context = {}
    return render(request, 'meals/index.html', context)
 

def dishes(request):
    dishes = Meal.objects.all
    context = {
        "dishes": dishes
    }
    return render(request, 'meals/dishes.html', context)

def about(request):
    context = {}
    return render(request, 'meals/about.html', context) 

def menu(request):
    mainMenu = Meal.objects.all
    context = {
        "mainMenu": mainMenu
    }
    return render(request, 'meals/menu.html', context)

def newMeal(request):
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance
            context = {
                "form": form,
                "image_obj": image_obj
            }
            return render(request, 'meals/new_meal.html', context)
        return redirect('meals/dishes.html')
    else:
        form = MealForm()
        context = {
            "form": form
        }
    return render(request, 'meals/new_meal.html', context)                   
