from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)# admin.site.register(Post), performs the same functions
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] 
    #The list_display attribute allows you to specify the model fields that you want to to display on the list page of administration objects
    list_filter = ['status', 'created', 'publish', 'author']
    #Now the list page contains a right sidebar that allows you to filter results by the fields included in the list_filter attribute
    search_fields = ['title', 'body']
    #A search bar appears on the page. This is caused by the fact that we have defined a list of fields that can be searched using the attribute search_fields
    prepopulated_fields = {'slug': ('title',)}
    #When you enter the title of a new post, the slug field is automatically populated. You have told Django to prepopulate the slug field with the data entered in the title field using the prepopulated_fields attribute(Add Menu)
    raw_id_fields = ['author']
    #The author field is now displayed by a search widget, which will be more acceptable than selecting from a dropdown list when you have thousands of users. This is achieved with the raw_id_fields attribute
    date_hierarchy = 'publish'
    #Just below the search bar are navigation links to navigate through the date hierarchy; this is defined by the date_hierarchy attribute(Add Menu) 
    ordering = ['status', 'publish']
    #You can also see that by default, posts are ordered by STATUS and PUBLISH columns. The ordering attribute has been used to the sorting criteria that will be used by default