from django.shortcuts import render,get_object_or_404,redirect
from blogpy.models import Post
from comments.models import Comments
from comments.forms import CommentForm
# Create your views here.

def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk = post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comments_set.all()
            context = {'post':post,
                       'form':form,
                       'comment_list':comment_list
                       }
        return render(request,'blogpy/detail.html',context=context)
    return redirect(post)