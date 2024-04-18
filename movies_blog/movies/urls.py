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
    path('create_new/', views.create_new, name='create_new'),
    path('img_upload/', views.img_upload, name='img_upload'),
    path('save/', views.save, name='save'),
    # path('create_movie/', views.create_movie, name='create_movie'),
    path('movie_info/<int:movie_pk>', views.movie_info, name='movie_info'),
    path('delete_movie/<int:movie_pk>', views.delete_movie, name='delete_movie'),
    path('edit_movie/<int:movie_pk>', views.edit_movie, name='edit_movie'),
    path('create_comment/<int:pk>', views.create_comment, name='create_comment'),
    path('<int:movie_id>/comments/<int:comment_id>/delete/', 
         views.delete_comment, name='delete_comment'),
]
