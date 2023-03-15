from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('qwer/', views.qwer, name='qwer'),
    path('asdf/', views.asdf, name='asdf'),
]
