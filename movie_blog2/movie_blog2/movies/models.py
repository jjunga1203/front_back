from django.db import models

# Create your models here.
class Movie(models.Model):
    # 각 변수값은 필드명
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_open = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
