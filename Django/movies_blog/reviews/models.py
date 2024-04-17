from django.db import models

# Create your models here.
class Review(models.Model):
    movie_title = models.CharField(max_length=20)
    review_title = models.TextField()
    review_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)