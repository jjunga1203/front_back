from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews
    }
    return render(request, 'reviews/index.html', context)

def delete(request, review_idx):
    review = Review.objects.get(pk=review_idx)
    if review:
        review.delete()
    return redirect('reviews:index')

def update(request, review_idx):
    review = Review.objects.get(pk=review_idx)
    if request.method == "POST": 
        form = ReviewForm(request.POST, instance = review)
        if form.is_valid():
            form.save()
            return redirect("reviews:detail", review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        "form": form,
        "review": review
    }
    return render(request, "reviews/update.html", context)


def detail(request, review_idx):
    review = Review.objects.get(pk=review_idx)
    context = {
        "review": review
    }
    return render(request, "reviews/detail.html", context)


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect("reviews:index")
    else:
        form = ReviewForm()
    context = {
        "form": form
    }
    return render(request, 'reviews/create.html', context)