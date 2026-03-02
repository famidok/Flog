from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Profile

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    user_info = get_object_or_404(Profile, nickname='Famidok')
    return render(request, 'about.html', {'user_info': user_info})


def CV(request):
    user_info = get_object_or_404(Profile, nickname='Famidok')
    context = {
        'user_info': user_info,
    }
    return render(request, 'CV.html', context)

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

# def projects(request):
#     return render(request, 'projects.html')
#
# def contact(request):
#     return render(request, 'contact.html')
#
# def links(request):
#     return render(request, 'links.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})