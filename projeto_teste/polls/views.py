from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm



def post_list(request):
    posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('published_date')        

    return render(request, 'blog.html', {'posts' : posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            author = User.objects.all()[0]

            post = Post.objects.create(author = author, title = title, text = text)
            post.publish()
            return redirect('/')
            
    
    form = PostForm()
    return render(request, 'post_new.html', {'form' : form})