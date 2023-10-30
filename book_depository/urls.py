from django.urls import path
from . import views

app_name = 'books'#The above source code defines the application namespace using the app_name variable

urlpatterns = [
    # post submissions
    path('', views.post_list, name='post_list'),#The first URL pattern takes no arguments and is relative to the post_list view
    path('<int:id>/', views.post_detail, name='post_detail'),
    #The second template relates to the post_detail view and takes only one id argument,
    # which matches an integer specified by the int path converter integer.
]
