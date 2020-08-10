from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from post_app.forms import *
from post_app.models import *
from login_app.models import *


# Create your views here.

@login_required
def index(request):
    userpost=post.objects.filter(author=request.user)
    follower_list = follow.objects.filter(follower= request.user)
    posts = post.objects.filter(author__in=follower_list.values_list('following'))
    if request.method=='GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'post_app/index.html', context={'follower_list': follower_list, 'search':search, 'result':result, 'postlist':posts, 'userpost':userpost})

@login_required
def createpost(request):
    form = newpost()
    if request.method == 'POST':
        form = newpost(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('post_app:index'))
    return render(request, 'post_app/createpost.html', context={'form':form})

@login_required
def liked(request, pk):
    posts = post.objects.get(pk=pk)
    users = request.user
    already_liked = like.objects.filter(lpost=posts, user=users)
    if not already_liked:
        liked_post = like(lpost=posts, user=users)
        liked_post.save()
        already_disliked = dislike.objects.filter(dpost=posts, user=users)
        already_disliked.delete()
    return HttpResponseRedirect(reverse('post_app:index'))

@login_required
def disliked(request, pk):
    posts = post.objects.get(pk=pk)
    users = request.user
    already_disliked = dislike.objects.filter(dpost=posts, user=users)
    if not already_disliked:
        disliked_post = dislike(dpost=posts, user=users)
        disliked_post.save()
        already_liked = like.objects.filter(lpost=posts, user=users)
        already_liked.delete()
    return HttpResponseRedirect(reverse('post_app:index'))
