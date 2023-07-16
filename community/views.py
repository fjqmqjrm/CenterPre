from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import redirect
# from .models import User
from .models import Post
from .forms import PostForm
# Create your views here.

def buy_review(request):
    return render(request, "community/review.html")

def freeboard_view(request):
    posts = Post.objects.all()
    return render(request, "community/freeboard.html", {'posts': posts})

def community_view(request):
    return render(request, "community/community.html")

def freeboard_list(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'community/freeboardDetail.html', {'post': post})

@login_required
def freeboard_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # return redirect('community:freeboard')
            return render(request, 'community/freeboardDetail.html', {'post': post})
    else:
        form = PostForm()
    return render(request, 'community/freeboardPost.html', {'form': form})

@login_required
def freeboard_edit(request, pk):
    post = Post.objects.get(id=pk)

    # 권한 검사
    if post.author != request.user:
        return HttpResponseForbidden("You don't have permission to edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'community/freeboardDetail.html', {'post': post})
    else:
        form = PostForm(instance=post)
    return render(request, 'community/freeboardPost.html', {'form': form})

