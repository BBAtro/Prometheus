from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.

"""The request parameter represents the HTTP request coming from the client (browser) to your web server.
In Django, for example, this is the HttpRequest object, which contains all the information about the request, including form data, URL parameters, headers, and more."""
def post_list(request):
    """The post_list view takes a request object as a single parameter. 
    The specified parameter is required for all functions-representations."""
    post_list = Post.published.all()#This view retrieves all posts with PUBLISHED status using the published manager
    paginator = Paginator(post_list, 3)
    # Pagination with 3 posts per page
    #We create an instance of the Paginator class with the number of objects returned per page.
    page_number = request.GET.get('page', 1)
    """We retrieve the HTTP GET parameter page and store it in the variable page_number.
      This parameter contains the requested page number.
        If the page parameter is not in the GET parameters of the request,
        we use the the default value of 1 to load the first page of results."""
    try:
      posts = paginator.page(page_number)
      #We get the objects for the desired page by calling the method page() method of the Paginator class
    except PageNotAnInteger:
      #If page_number is not an integer, then output the first page
      posts = paginator.page(1)
    except EmptyPage:
      #If page_number is out of range, then output the last page
      posts = paginator.page(paginator.num_pages)

    return render(request, #We use the shortcut render() function provided by Django to render a list of posts in a given pattern.
                  'books/post/list.html',
                  {'posts': posts}) 

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                        status = Post.Status.PUBLISHED,
    #match the URL parameters, and use them to retrieve the corresponding Post object
                        slug=post,
                        publish__year=year,
                        publish__month=month,
                        publish__day=day)
    """The specified function retrieves an object matching the passed parameters,
     or an HTTP exception with a status code of 404 (not found) if the object is not found"""
    return render(request,
                  'books/post/detail.html',
                  {'post': post})