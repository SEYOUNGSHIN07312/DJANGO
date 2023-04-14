from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from .models import Article
from django.core import serializers
from .serializers import ArticleSerializer

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    # articles 결과값 = 쿼리셋
    articles = Article.objects.all()
    articles_json = {}
    # 혹은 빈 리스트 생성 후 append로 추가

    for article in articles:
        articles_json[article.pk] = (
            {
                # 'id':article.pk,
                'title':article.title,
                'content':article.content,
                'created_at':article.created_at,
                'updated_at':article.updated_at,
            }
        )

    # safe=True일 경우는 딕셔너리 형태만 올 수 있음
    # safe=False로 변경했을 경우 형태에 상관없이 응답 가능
    return JsonResponse(articles_json)


def article_json_2(request):
    articles = Article.objects.all()
    # serialize는 articles를 json으로 바꿔주는 함수

    '''
    DB에서 데이터를 꺼낼때는 serialize해줌
    왜냐면 프론트에는 쿼리셋이 존재하지 않는 타입임
    
    request로 json이 들어올때는 deserialize해줌
    json을 쿼리셋으로 변환한 후 DB에 저장해줌

    '''
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')


def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)