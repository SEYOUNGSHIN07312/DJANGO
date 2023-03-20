from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles':articles
    }
    
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(id=pk)
    
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # DB에 새로운 Article 저장
    # Article.objects.create(title=title, content=content)

    article = Article(title=title, content=content)
    # ~~~~ 중간 처리 (유효성 검사 과정) ~~~~
    article.save()
        
    return redirect('articles:index')

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article':article,
    }
        
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)