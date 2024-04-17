from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie

        fields = ['title', 'content', 'is_open']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'제목 입력창'}),
            'content': forms.Textarea(attrs={'class':'my-class'}),
        }
        error_messages = {
            'title': {
                'max_length': '입력 길이를 초과했습니다.'
            }
        }

# 댓글입력받기 위해  Comment ModelForm 정의
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )