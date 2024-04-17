from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_open = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)