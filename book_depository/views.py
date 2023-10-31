from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

"""The request parameter represents the HTTP request coming from the client (browser) to your web server.
In Django, for example, this is the HttpRequest object, which contains all the information about the request, including form data, URL parameters, headers, and more."""
def post_list(request):
    """The post_list view takes a request object as a single parameter. 
    The specified parameter is required for all functions-representations."""
    posts = Post.published.all()#This view retrieves all posts with PUBLISHED status using the published manager
    return render(request, #We use the shortcut render() function provided by Django to render a list of posts in a given pattern.
                  'books/post/list.html',
                  {'posts': posts}) 

def post_detail(request,id):
    post = get_object_or_404(Post,
                        id=id,
                        status = Post.Status.PUBLISHED)
    """The specified function retrieves an object matching the passed parameters,
     or an HTTP exception with a status code of 404 (not found) if the object is not found"""
    return render(request,
                  'books/post/detail.html',
                  {'post': post})