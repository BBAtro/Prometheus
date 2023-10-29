from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model): #class that will be responsible for communication with the database and posts in the application

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250) #that line created in database field "title" typed VARCHAR with parametres lenth
    slug = models.SlugField(max_length=250) #that line created in database field "slug" typed VARCHAR with parametres lenth
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField() #that line created in database field "body" typed TEXT
    publish = models.DateTimeField(default=timezone.now) #created database field DateTime to store the date and time the post was published with parametres of current time zone
    created = models.DateTimeField(auto_now_add=True) #db field datetime created post 
    updates = models.DateTimeField(auto_now=True) #db field datetime updated post (overwritten)
    status = models.CharField(max_length=2, 
                              choices=Status.choices,
                              default=Status.DRAFT)
    """We defined the Status enumerated class by subclassing the
    models.TextChoices class. The available options for post status are.
    DRAFT and PUBLISHED. Their corresponding values are DF and PB, and their labels or readable names are Draft and Published.
    labels or readable names are Draft and Published."""


    class Meta: #meta class for model metadata definition
        ordering = ['-publish'] #sorts posts by publication time
        indexes = [
            models.Index(fields=['-publish']), #add index to database on the field "publish"
        ]

    def __str__(self): #method for displaying information from the title field
        return self.title 