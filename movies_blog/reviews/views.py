from django.shortcuts import render, redirect
from .models import Review, Review_Comment
from .forms import ReviewForm, Review_CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews,
    }
    return render(request, 'reviews/index.html', context)

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comments = review.review_comments.all()
    comment_form = Review_CommentForm()

    print(review_pk)
    context = {
        'form':review,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)

def create(request):
    
    # 신규리뷰 저장
    if request.method == 'POST':
        print(request.FILES)
        form = ReviewForm(request.POST, request.FILES)  # 이미지 업로드 로 수정함.
        
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review.pk)
        context = {
            'form':form
        }
        return render(request, 'reviews/create.html', context)
    
    # 신규리뷰 열기
    form = ReviewForm()
    context = {
        'form':form
    }
    return render(request, 'reviews/create.html', context)

def edit(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.user != review.user:
        return redirect('reviews:index')
    
    # 수정 후 제출 클릭
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            review = form.save()
            return redirect('reviews:detail', review_pk)
        context = {
            'form':form
        }
        # return render(request, 'reviews:edit', context)
        return redirect('reviews:detail', review_pk=review_pk)

    # 수정 버튼 클릭
    
    form = ReviewForm(instance=review)
    context = {
        'form':form,
        'review':review,
    }
    return render(request, 'reviews/edit.html', context)

def delete(request, review_pk):
    Review.objects.filter(pk=review_pk).delete()
    return redirect('reviews:index')

# @login_required
# 댓글 생성
def create_comment(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = Review_CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('reviews:detail', pk)
    context = {
        'review': review,
        'comment_form': comment_form
    }
    return render(request, 'reviews/detail.html', context)

# 내 댓글 삭제
def delete_comment(request, review_id, comment_id):
    comment = Review_Comment.objects.get(pk=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect('reviews:detail', review_id)

# 리뷰글에 좋아요 하기
def review_like(request, review_id):
    review = Review.objects.get(pk=review_id)

    # 이미 좋아요 했다면 좋아요를 취소하도록 함.
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user, through_defaults={'memo':
                                                        '메모'})
        is_liked = True

    context = {
        'is_liked': is_liked,
        'review_id': review.pk,
        'like_cnt': review.like_users.count()
    }

    return JsonResponse(context)
    # return redirect('reviews:index')


# 좋아요 수를 누르면 좋아요 한 유저가 보이도록
def review_like_users(request, review_idx):
    review = Review.objects.get(pk=review_idx)
    like_users = review.like_users.all()
    context = {
        'like_users': like_users,
        'review': review,
    }
    return render(request, 'reviews/review_like_users.html', context)
