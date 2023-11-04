from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                        .filter(status=Post.Status.PUBLISHED)

class Post(models.Model): #class that will be responsible for communication with the database and posts in the application

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250) #that line created in database field "title" typed VARCHAR with parametres lenth
    slug = models.SlugField(max_length=250, #that line created in database field "slug" typed VARCHAR with parametres lenth
                            unique_for_date='publish')
                            #When using the unique_for_date parameter, the slug field must be unique for the date stored in the publish field.
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField() #that line created in database field "body" typed TEXT
    publish = models.DateTimeField(default=timezone.now) 
    #created database field DateTime to store the date and time the post was published with parametres of current time zone
    created = models.DateTimeField(auto_now_add=True) #db field datetime created post 
    updates = models.DateTimeField(auto_now=True) #db field datetime updated post (overwritten)
    status = models.CharField(max_length=2, 
                              choices=Status.choices,
                              default=Status.DRAFT)
    """We defined the Status enumerated class by subclassing the
    models.TextChoices class. The available options for post status are.
    DRAFT and PUBLISHED. Their corresponding values are DF and PB, and their labels or readable names are Draft and Published.
    labels or readable names are Draft and Published."""

    objects = models.Manager() 
    #By default, each model uses the objects manager. This manager retrieves all objects from the database.
    published = PublishedManager()
    #However, it is possible to define application-specific model managers.

    class Meta: #meta class for model metadata definition
        ordering = ['-publish'] #sorts posts by publication time
        indexes = [
            models.Index(fields=['-publish']), #add index to database on the field "publish"
        ]

    def __str__(self): #method for displaying information from the title field
        return self.title 
    
    """Canonical URLs allow you to specify the URL of a master copy of a page. 
    Django allows you to implement the get_absolute_url() method in your own models,
      which returns the canonical URL of an object."""   
    def get_absolute_url(self):
        return reverse("books:post_detail",
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
    """The reverse() function will generate the URL dynamically by applying the URL name defined in the URL templates.
      the URL name defined in the URL templates."""
    