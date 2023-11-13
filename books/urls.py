from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous url
    # path('login/', views.user_login, name='login'),

    # urls to login and logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.dashboard, name='dashboard'),
]