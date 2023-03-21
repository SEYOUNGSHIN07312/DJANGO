from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


# GET 방식
# def new(request):
#     return render(request, 'articles/new.html')


def create(request):
    # POST 방식의 요청이 들어오면 == 생성 form 입력받음
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:index')
    # GET 방식의 요청이 들어오면 == 생성 페이지 렌더링
    else:
        return render(request, 'articles/create.html')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# GET 방식
# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article}
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    # POST 방식의 요청이 들어오면 == 수정 form 입력받음
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', pk=article.pk)
    # GET 방식의 요청이 들어오면 == 수정 페이지 렌더링
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)
