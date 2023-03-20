from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # DB 변경되지 않고 Django에서 보여줄 형식 지정하는 것
    def __str__(self):
        return f'{self.id}번째글 - {self.title}'