from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #The form = LoginForm(request.POST) instruction creates an instance of the form with the passed data
        if form.is_valid(): 
            #the form is validated by the form.is_valid() method. If it is invalid, 
            #then form errors will be displayed later in the template
            # (for example, if the user has not filled in one of the fields)
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])
            """if the data passed for processing is valid,
             the user is authenticated against the database using the authenticate() method.
            This method accepts a request object,
            username and password parameters and returns a User object if the user was successfully authenticated or None otherwise."""
            if user is not None:
                if user.is_active:
                    """if the user is successfully authenticated,
                    the user status is checked by referring to the is_active attribute.
                    The specified attribute belongs to the User model of the Django web framework.
                    If the user is not active, an HttpResponse with the Disabled account message is returned"""
                    login(request, user)
                    """If the user is active, the user is logged in.
                    The user is specified in a session by calling the login() method.
                    This returns the message Authenticated successfully"""
                    return HttpResponse('Authenticated successfully')
                    # form.add_error(None, 'Authenticated successfully')
                else:
                    form.add_error(None, 'Disabled account')
            else:
                form.add_error(None, 'Invalid login')
                #If the user was not successfully authenticated,
                # a raw HttpResponse with the message Invalid login is returned
    else:
        form = LoginForm()
    return render(request, 'books/login.html', {'form': form})


"""If the user is authenticated, it executes a decorated representation; 
if the user is not authenticated, 
it redirects the user to the login URL with the originally requested URL as a GET parameter named next"""
@login_required #decorator, checks the authentication of the current user
def dashboard(request):
    return render(request,
                  'books/dashboard.html',
                  {'section': 'dashboard'})