from django.shortcuts import render
import random

# Create your views here.
def index(request):
    
    name = 'aiden'
    return render(request, 'APP1/index.html', {'name' : name})

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name':'Bacon',
    }
    
    context = {
        'foods' : foods,
        'info' : info,
        }
    
    return render(request, 'APP1/greeting.html', context)

def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥',]
    pick = random.choice(foods)
    context = {
        'foods':foods,
        'pick':pick,
    }
    return render(request, 'APP1/dinner.html', context)
    