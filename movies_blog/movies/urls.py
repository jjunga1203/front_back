"""
URL configuration for movies_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'movies'

urlpatterns = [

    path('movies/', views.index, name='index'),
    path('', views.index, name='index'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('submit_movie/', views.submit_movie, name='submit_movie'),
    path('<str:movie>', views.movie_info, name='movie_info'),
    # path('movie_info/', views.movie_info, name='movie_info'),
    # path('<str:movie>', views.movie_detail, name="movie_detail"),
]
