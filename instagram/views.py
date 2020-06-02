from django.shortcuts import render
from django.http  import HttpResponse
from .models import Post
from .forms import NewsLetterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
@login_required(login_url='/accounts/login/')
def profile(request):
    profile = profile.objects.all
    return render(request, 'profile.html', {"instagram":instagram,"letterForm":form})

def other_profile(request,id):
    profile_user=User.objects.filter(id=id).first()
    posts=Post.objects.all()
    
    return HttpResponse(html)

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_post = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"post": searched_post})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})