from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class Account(models.Model):
#     login_id = models.CharField(max_length=20)
#     login_pw = models.CharField(max_length=20)

#     created_at = models.DateField(auto_now_add=True)

class User(AbstractUser):

    # 프로젝트를 진행하다 이후에 이런것들을 생성함.
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
