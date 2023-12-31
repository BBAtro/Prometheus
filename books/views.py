from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm
from .models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new object, but not save
            new_user = user_form.save(commit=False)
            #set password
            new_user.set_password(user_form.cleaned_data['password'])
            #save User object
            new_user.save()
            #Create user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'books/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'books/register.html',
                  {'user_form': user_form})


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

"""Added an edit view so that users can edit their personal information. 
Added a login_required decorator to it, since only authenticated users can edit their profiles."""
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            """In order to validate the transmitted is_valid() method of both forms is called. 
            If both forms contain valid data, both forms are saved by calling the save() method, 
            to update the corresponding objects in the database"""
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль обновлен')
        else:
            messages.error(request, 'Ошибка обновления вашего профиля')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'books/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})