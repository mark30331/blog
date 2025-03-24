from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
# first thing to do is to create a database if storing of some form of data/info is needed in your application

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post_Table.Status.PUBLISHED)
    
class Post_Table(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft' # values are ['DF', 'PB'] are stored in the database and 
        # the labels are ['Draft', 'Published'] are shown on the admin panel
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish') # the slug field is now required to be unique for the data stored in the
    # publish field. 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True) # a user can have multiple posts.
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True , null=True)# while the auto_now_add sets the field's date only when you create the data.
    updated = models.DateTimeField(auto_now=True) # The auto_now parameter sets the date every time you change or update data
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    objects = models.Manager() # default manager
    published = PublishedManager() # our custom manager
    # in this case we are using both model managers. 

    tags = TaggableManager()

    class Meta:
        verbose_name = 'post' # used to change the name or how it appears
        ordering = ['-publish'] # used to change the order from ascending to descending using the minus on the UI not the DB
        indexes = [
            models.Index(fields=['-publish']), # index the database in descending order according to publish
        ]

    def get_absolute_url(self): # this func reverses and builds the url dynamically using the url name defined in the url p.atterns 
        return reverse('blog:post_detail', args=[self.id,
                                                 self.slug])

    def __str__(self) -> str:
        return f'Title: {self.title}'
    
    
class Comment_Table(models.Model):
    post_table = models.ForeignKey(Post_Table, on_delete=models.CASCADE, related_name='comments') # a post can have multiple comments that why 
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self) -> str:
        return f'Comment by {self.name}'