from django.shortcuts import render
from .models import Post

# Create your views here.

"""The request parameter represents the HTTP request coming from the client (browser) to your web server.
In Django, for example, this is the HttpRequest object, which contains all the information about the request, including form data, URL parameters, headers, and more."""
def post_list(request):
    """The post_list view takes a request object as a single parameter. 
    The specified parameter is required for all functions-representations."""
    posts = Post.published.all()#This view retrieves all posts with PUBLISHED status using the published manager
    return render(request, #We use the shortcut render() function provided by Django to render a list of posts in a given pattern.
                  'book_depository/post/list.html',
                  {'posts': posts}) 