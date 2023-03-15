from django.shortcuts import render
import random

# Create your views here.
def index(request):
    
    names = ['shin', 'heo', 'jeon', 'choi',]
    name = random.choice(names)
    
    return render(request, 'articles/index.html', {'name':name})

def greeting(request):
    hellos = ['hi', '안녕', 'salut', 'hola',]
    hello = random.choice(hellos)
    names = ['shin', 'heo', 'jeon', 'choi',]
    name = random.choice(names)
    
    context = {
        'hello':hello,
        'name':name,
    }
    return render(request, 'articles/index.html', context)

def qwer(request):
    say = '하하하'
    return render(request, 'articles/qwer.html', {'say':say})

def asdf(request):
    say = '호호호'
    return render(request, 'articles/asdf.html', {'say':say})