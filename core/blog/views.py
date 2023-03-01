from django.shortcuts import render
from .models import Post
# Create your views here.
def blog_list(request):
    obj = Post.objects.all()
    return render(request, 'blog/post_list.html',{'obj':obj})


def blog_detil(request,id):
    obj = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html',{'obj':obj})
