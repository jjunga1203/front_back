from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_movie/', views.create_movie, name='create_movie'),
    path('save_movie/', views.save_movie, name='save_movie'),
    path('delete_movie/<int:movie_pk>/', views.delete_movie, name='delete_movie'),
    path('update_movie/<int:movie_pk>/', views.update_movie, name='update_movie'),
    path('edit_movie/<int:movie_pk>/', views.edit_movie, name='edit_movie'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
]