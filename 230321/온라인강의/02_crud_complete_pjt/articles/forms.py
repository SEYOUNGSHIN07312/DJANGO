from django import forms
from .models import Article

# model의 Textfield => 문자 입력받는 것은 똑같은데 보여지는 부분이 넓어지는 것
# widget = 보여지는 부분 변경
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        # Article의 모든 field를 그대로 가져옴
        fields = '__all__'
    
'''
    # 유효성 검사 함수 : clean_검사할항목
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'django' in title:
            return True
        return False
'''    