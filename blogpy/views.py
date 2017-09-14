from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category
import markdown
import pygments
from comments.forms import CommentForm

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    print(post_list)
    return render(request,'blogpy/index.html',context={'post_list':post_list})
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                              ])
    form = CommentForm()
    comment_list = post.comments_set.all()
    context ={'post':post,
              'form':form,
              'comment_list':comment_list}
    return render(request,'blogpy/detail.html',context=context)
def archives(request,year,month):
    post_list = Post.objects.filter(create_time__year=year,create_time__month=month)
    print(post_list)
    return render(request,'blogpy/index.html',context={'post_list':post_list})
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request,'blogpy/index.html',context={'post_list':post_list})