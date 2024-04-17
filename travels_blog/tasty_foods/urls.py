from django.urls import path
from . import views
app_name = 'tasty_foods'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasty_foods/', views.index, name='index'),
]
