from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    # 리뷰에 좋아요 한 사람 저장
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                        related_name='like_reviews', through='ReviewLikeUsers')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 이미지 컬럼 추가
    imgfile = models.ImageField(null=True, upload_to='UploadedFiles/%y/%m/%d/', blank=True)
    # img_uploaded_at = models.DateTimeField(auto_now = True)
    
    # content2 = models.TextField()

# 리뷰에 좋아요 기능을 넣기 위한 모델 생성
class ReviewLikeUsers(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    memo = models.TextField(null=True)

    class Meta:
        db_table = 'review_like_users'


class Review_Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_comments')
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
