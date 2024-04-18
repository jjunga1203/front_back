from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    user_list = get_user_model().objects.all()

    content = {
        'movies': movies,
        'users': user_list,
    }
    return render(request, 'movies/index.html', content)

# MovieForm 이용하기
def create_new(request):
    form = MovieForm()
    context = {
        'form':form
    }

    return render(request, 'movies/create.html', context)

# MovieForm 이용하기
# @login_required
def save(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            Movie = form.save()
            return redirect('movies:movie_info', Movie.pk)
        context = {
            'form':form
        }
        return render(request, 'movies/create.html', context)

    form = MovieForm()
    context = {
        'form':form
    }

    return render(request, 'movies/create.html', context)

# def create_movie(request):
#     if request.method == 'POST':
#         data = request.POST
#         movie = Movie()
#         # movie = form.save(commit=False)
#         # movie.user = request.user
#         # movie.save()

#         movie.title = data.get('movie_name')
#         movie.content = data.get('content')

#         if data.get('isopen') == 'on':
#             movie.is_open = True
#         else:
#             movie.is_open = False

#         movie.save()

#         return redirect('movies:index')

#     else:
#         return render(request, 'movies/add_movie.html')       

def edit(request, movie_pk):
    form = MovieForm()
    context = {
        'form':form
    }

    return render(request, 'movies/create.html', context)



def edit_movie(request, movie_pk):
    # 내용 수정하고 난 후 
    movie = Movie.objects.get(pk=movie_pk)
    
    # 글 작성자가 아닌 사람이 수정 못하도록 함.
    if request.user != movie.user:
        return redirect('movies:index')
    
    if request.method == 'POST':
        data = request.POST
        if data.get('isopen') == 'on':
            isopen = True
        else:
            isopen = False
        
        Movie.objects.filter(pk=movie_pk).update(
            title=data.get('movie_name'), 
            content=data.get('content'),
            is_open=isopen)
        return redirect('movies:movie_info', movie_pk=movie_pk)    
    else:
        # 수정 화면으로 이동
        movie = Movie.objects.get(pk=movie_pk)
        content = {
            'movie':movie
        }
        return render(request, 'movies/edit_movie.html', content)


def delete_movie(request, movie_pk):
    # 작성자만 삭제 가능
    movie = Movie.objects.filter(pk=movie_pk)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')

def movie_info(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.comments.all()  # 무비정보 보여줄때, 해당 무비의 하위 댓글 정보 모두 가져오기
    comment_form = CommentForm()
    content = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/movie_info.html', content)

# 댓글 작성하기
def create_comment(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)   # commit=False는 실제 저장은 안하고 객체만 생성
        comment.movie = movie # 댓글의 원본 movie 연결해 줌.
        comment.user = request.user
        comment.save()
        return redirect('movies:movie_info', pk)
    context = {
        'movie':movie,
        'comment_form': comment_form
    }
    return render(request, 'movies/movie_info.html', context)

# 댓글 삭제하기
def delete_comment(request, movie_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)

    if request.user == comment.user:
        comment.delete()
    return redirect('movies:movie_info', movie_id)


# 임시 테스트
def img_upload(request):
    return render(request, 'movies/img_upload.html')