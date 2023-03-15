from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('qwer/', views.qwer, name='qwer'),
]