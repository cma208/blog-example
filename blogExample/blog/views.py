from django.shortcuts import render, get_object_or_404
from .models import Post
# from django.http import Http404

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    print(posts)
    return render(request, 'blog/post/list.html', {'posts':posts})

def post_detail(request,id):
    # --------------------------------
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('Post does not exist')
    # --------------------------------
    # The last part of the code is replaced by the use of get_object_or_404, this raise a Http404 exception instead of a DoesNotExist exception when no object is found
    # --------------------------------
    
    # post is a dictionary [key, value] == ['post', posts_returned_by_get_object_or_404]
    post = get_object_or_404(Post, 
                            id=id, 
                            status=Post.Status.PUBLISHED)
    
    return render(request, 
                  'blog/post/detail.html', 
                  {'post':post})