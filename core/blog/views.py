from django.shortcuts import render
from .models import Post
# Create your views here.

#Get all the posts from database
def blog_list(request):
    obj = Post.objects.all()
    return render(request, 'blog/post_list.html',{'obj':obj})

#Get single post by id
def blog_detil(request,id):
    obj = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html',{'obj':obj})
