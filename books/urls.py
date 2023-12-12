from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous url
    # path('login/', views.user_login, name='login'),

    # urls to login and logout
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),

#     #urls to change password
#     path('password-change/',
#          auth_views.PasswordChangeView.as_view(),
#          name='password_change'),
#     path('password-change/done/',
#          auth_views.PasswordChangeDoneView.as_view(),
#          name='password_change_done'),

#     #urls to password-reset
#     path('password-reset/', 
#          auth_views.PasswordResetView.as_view(),
#          name='password_reset'),
#     path('password-reset/done/', 
#          auth_views.PasswordResetDoneView.as_view(),
#          name='password_reset_done'),
#     path('password-reset/<uidb64>/<token>/', 
#          auth_views.PasswordResetConfirmView.as_view(),
#          name='password_reset_confirm'),
#     path('password-reset/complete/', 
#          auth_views.PasswordResetCompleteView.as_view(),
#          name='password_reset_complete'),
     
    #urls to authentication
    path('', include('django.contrib.auth.urls')),

    #url for show profile
    path('', views.dashboard, name='dashboard'),

    #url for registration form
    path('register/', views.register, name='register'),

    #url for edit account
    path('edit/', views.edit, name='edit'),
]