from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import User
from django.http import JsonResponse

# Create your views here.
def change_password(request, user_id):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:index', request.user.id)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)

# update 반드시 로그인 상태가 필수조건
@login_required
def update(request):
    # # 로그인하지 않은 경우, 정보수정 제한
    # if not request.user.is_authenticated:
    #     return redirect('accounts:index')


    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index', request.user.id)
    else:
        print(request.user)
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)


def login(request):
    # 이미 로그인한 경우, 정보화면으로 이동
    if request.user.is_authenticated:
        return redirect('accounts:index', request.user.id)
    
    # 로그인 시도
    # 세션을 생성! 하니까 POST
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index', request.user.id)

    form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

# logout은 반드시 로그인 상태가 필수조건
@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    # 이미 로그인한 경우, 회원가입 로직 실행 막기
    if request.user.is_authenticated:
        return redirect('accounts:index', request.user.id)
    
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def index(request, user_idx):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    user = User.objects.get(pk=user_idx)
    reviews = user.reviews.all()
    comments = user.review_comments.all()
    context = {
        'reviews': reviews,
        'comments': comments, 
        'target_user':user,
    }

    return render(request, 'accounts/index.html', context)

# 탈퇴는 반드시 로그인 상태가 필수조건
@login_required
def delete(request):
    request.user.delete()
    return redirect('accounts:login')


# 개인 프로파일 화면
def profile(request, username):
    # print(username)
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    reviews = request.user.reviews.all()
    comments = request.user.review_comments.all()
    user = get_user_model().objects.get(username=username)

    print(user.like_reviews.all)
    context = {
        'user':user,
        'reviews': reviews,
        'comments': comments, 
    }

    return render(request, 'accounts/profile.html', context)

# 팔로우 기능
def follow(request, user_idx):
    user = get_user_model().objects.get(pk=user_idx)

    # 본인을 팔로우할 수 없음
    if request.user == user:
        return redirect('accounts:index', user.id)
    
    # 팔로우한 사람이라면 , 팔로우 취소 
    # axios 이용한 코드로 변경
    if user.followers.filter(pk=request.user.id).exists():
        user.followers.remove(request.user)
        is_followed = False
    else:
        user.followers.add(request.user)
        is_followed = True
    
    # 팔로우 성공을 JSON 형태로 반환
    context = {
        'is_followed': is_followed,
        'following_cnt': user.followings.count(),
        'follower_cnt': user.followers.count(),
    }
    
    # return redirect('accounts:index', user.id)
    return JsonResponse(context)

