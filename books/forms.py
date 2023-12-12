from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    #Form to login user
    
    #Add a new fields in form
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    #Form to registration user

    #Add a new fields in form
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    #if password on fields dont match to clean
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
    
class UserEditForm(forms.ModelForm):
    """UserEditForm will allow users to edit their first name, 
    last name, and email address, which are attributes of Django's built-in User model"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    """ProfileEditForm will allow users to edit profile data stored in an application-specific Profile model.
      Users will be able to edit their date of birth and upload the image to the site as a profile picture"""
    class Meta:
        model = Profile
        fields = ['date_of_birth']