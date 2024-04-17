from django.contrib import admin
# from .models import Account
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.
# admin.site.register(Account)

admin.site.register(User, UserAdmin)