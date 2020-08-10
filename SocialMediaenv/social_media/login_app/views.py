from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from login_app.forms import *
from login_app.models import *

# Create your views here.

def signup(request):
    diction = {}
    form = createnewuser()
    registered = False
    if request.method == 'POST':
        form=createnewuser(data=request.POST)
        if form.is_valid():
            user=form.save()
            registered = True
            user_profile = userprofile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('login_app:login'))
    diction.update({'registered': registered})
    diction.update({'form':form})
    return render(request, 'login_app/signup.html', context=diction)

def userlogin(request):
    diction={}
    form = Authenticateuser()
    if request.method == 'POST':
        form = Authenticateuser(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('post_app:index'))
    diction.update({'form':form})
    return render(request, 'login_app/login.html', context=diction)

@login_required
def edit_profile(request):

    current_user = userprofile.objects.get(user=request.user)
    form = editprofile(instance=current_user)
    if request.method == 'POST':
        form = editprofile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            form = editprofile(instance=current_user)
            return HttpResponseRedirect(reverse('login_app:profile'))

    return render(request, 'login_app/editprofile.html', context={'form':form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:login'))

@login_required
def profile(request):
    diction = {}
    return render(request, 'login_app/profile.html', context=diction)

@login_required
def authors(request, username):
    author = User.objects.get(username=username)
    already_follow = follow.objects.filter(follower=request.user, following=author)
    if author==request.user:
        return HttpResponseRedirect(reverse('login_app:profile'))
    return render(request, 'login_app/authors.html', context={'author':author, 'already_follow':already_follow})

@login_required
def followed(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_follow = follow.objects.filter(follower=follower_user, following=following_user)
    if not already_follow:
        followed_user = follow(follower=follower_user, following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('login_app:authors', kwargs={'username':username}))

@login_required
def unfollowed(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_follow = follow.objects.filter(follower=follower_user, following=following_user)
    already_follow.delete()
    return HttpResponseRedirect(reverse('login_app:authors', kwargs={'username':username}))


