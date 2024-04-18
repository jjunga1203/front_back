from django import forms
from .models import Review, Review_Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = ("movie_title", "title", "content", 'imgfile')

        widgets = {
            'movie_title':forms.TextInput(attrs={'placeholder':'영화 제목', 'class': 'movie-title'}),
            'title':forms.TextInput(attrs={'placeholder':'리뷰 제목', 'class': 'review-title'}),
            'content':forms.Textarea(attrs={"placeholder" : "리뷰 내용을 입력하세요"}),
        }
        labels = {
            'movie_title': '영화 제목',
            'title': '리뷰 제목',
            'content': '리뷰 내용',
            'imgfile': '이 미 지',
        }


class Review_CommentForm(forms.ModelForm):
    class Meta:
        model = Review_Comment
        fields = ('content',)