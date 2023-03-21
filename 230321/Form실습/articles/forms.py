from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)

# VS

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # 빼고 싶은 속성이 있다면 exclude 속성 사용 -> 튜플 형식(마지막 쉼표)
        # exclude = ('title',)