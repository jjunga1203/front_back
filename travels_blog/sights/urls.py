from django.urls import path
from . import views
app_name = 'sights'

urlpatterns = [
    path('sights/', views.index, name='index'),
    path('', views.index, name='index'),
    
]
