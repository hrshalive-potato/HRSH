from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

from .models import Post,Comment

# Post List view
def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request,'blog/post_list.html',{'posts':posts})

# Single Post view
def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    comments = post.comments.all().order_by('-created_at')
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request,'You must sign in to comment!')
            return redirect('account_login')
        body =  request.POST.get('body')
        if body:
            Comment.objects.create(post=post,author=request.user,body=body)
            messages.success(request,'Comment posted successfully!')
        else:
            messages.error(request,'Comment cannot be empty!')
    return render(request,'blog/post_detail.html',{'post':post,'comments':comments})
