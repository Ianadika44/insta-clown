from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Post
from django import forms
from .forms import NewsLetterForm,NewPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    posts = Post.objects.all
    
    
    return render(request, 'profile.html', {"posts":posts})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('new_post.html')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})
def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_post = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"post": searched_post})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})