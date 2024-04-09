from django.shortcuts import render

# Create your views here.
def index(request):
    content = {
        'test': '123'
    }
    return render(request, 'movies/index.html', content)

def add_movie(request):
    content = {

    }

    return render(request, 'movies/add_movie.html', content)

def submit_movie(request):
    data = request.GET
    print(data.get('movie_name'))
    content = {
        'add_movie_name': data.get('movie_name')
    }

    return render(request, 'movies/add_result_movie.html', content)