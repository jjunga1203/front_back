from django import forms
from .models import Review
class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ("movie_title", "review_title", "review_content")
        widgets = {
            'movie_title': forms.TextInput(attrs={"placeholder" : "영화 제목을 입력하세요", 'class': 'movie-title'}),
            'review_title': forms.TextInput(attrs={"placeholder" : "리뷰 제목을 입력하세요", 'class': 'review-title'}),
            'review_content': forms.Textarea(attrs={"placeholder" : "리뷰 내용을 입력하세요"}),
        }
        labels = {
            'movie_title': '영화 제목',
            'review_title': '리뷰 제목',
            'review_content': '리뷰 내용'
        }
