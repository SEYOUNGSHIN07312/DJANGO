from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    
    context ={
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        article = Article(title=title, content=content)
        article.save()
        
        return redirect('articles:index')
    else:
        return render(request, 'articles/create.html')

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')
    # if request.method == 'POST':
    #     article.delete()
    #     return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.id)

def edit(request, id):
    article = Article.objects.get(id=id)
    
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)
    
def update(request, id):
    article = Article.objects.get(id=id)
    
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.id)
    else:
        context = {
            'article': article,
        }
        return render(request, 'articles/update.html', context)