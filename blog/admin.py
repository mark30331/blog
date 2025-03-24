from django.contrib import admin
from .models import Post_Table, Comment_Table
# Register your models here.

@admin.register(Post_Table) # the same as admin.site.register(Posts_Table)
class Posts_Table_Admin(admin.ModelAdmin): # this class is for customization of the django admin page
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # customization
    list_filter = ['status', 'created', 'publish', 'author'] #this tell django-admin we want to use filters 
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug':('title',)}# this will automatically fill the slugfield when creating a new post using the title. 
    raw_id_fields = ['author']
    date_hierarchy = 'publish' # this orders the posts by date hierarchy
    ordering = ['status', 'publish']

    
@admin.register(Comment_Table)
class Comment_Table_Admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post_table', 'created', 'active']
    list_filter = ['active','created','updated']
    search_fields = ['name','email','body']