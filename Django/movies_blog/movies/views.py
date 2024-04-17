from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.
def index(request):
    # movie = request.GET.get('movie_pk')
    movie_list = Movie.objects.all()
    context = {
        # 'movie': movie_pk
        'movie_list': movie_list
    }
    return render(request, 'movies/index.html', context)

def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie

    }
    return render(request, 'movies/movie_detail.html', context)


def create_movie(request):
    
    return render(request, 'movies/create_movie.html')



def save_movie(request):

    movie_title = request.POST.get('movie_title')
    movie_content = request.POST.get('movie_content')
    is_open = False

    movie = Movie(title=movie_title, content=movie_content, is_open=is_open)
    movie.save()

    return redirect('movies:movie_detail', movie.pk)
    # return render(request, 'movies/create_movie.html')


def delete_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')

def update_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/update_movie.html', context)

def edit_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    movie_title = request.POST.get('movie_title')
    movie_content = request.POST.get('movie_content')

    movie.title = movie_title
    movie.content = movie_content
    movie.save()

    return redirect('movies:movie_detail', movie.pk)