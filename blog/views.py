from django.shortcuts import render, redirect ,get_object_or_404
from .models import Post_Table, Comment_Table
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.generic import ListView
from .forms import CommentForm
from django.views.decorators.http import require_POST

def post_list(request):
    posts = Post_Table.published.all() # get all published posts
    paginator = Paginator(posts, 3) # 3 posts per page
    page_number = request.GET.get('page',1) # We retrieve the
    #page GET HTTP parameter and store it in the page_number variable.
    # This parameter contains the requested page number. 
    #If the page parameter is not in the GET parameters of the request,
    # we use the default value 1 to load the first page of results.
    try:
        posts = paginator.page(page_number)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts' : posts,
        # 'all_posts': all_posts,
    }
   
    return render(request, 'blog/post/list.html', context)

# class PostListView(ListView):
#     queryset = Post_Table.published.all() # get all published posts
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'


def post_detail(request, id, slug):
    post = get_object_or_404(Post_Table, status = Post_Table.Status.PUBLISHED,
                             pk = id,
                             slug = slug) # This gets the post using the id and slug from the database
    comments = post.comments.filter(active = True) # this retrieves the comments using the related name in Comment_Table
    form = CommentForm() # this is the empty comment form. 
    context = {
        'post' : post,
        'form': form,
        'comments':comments,
    }
    return render(request, 'blog/post/detail.html', context)

@require_POST #We use the require_POST decorator provided by Django to only allow POST requests for this view. 
# Django allows you to restrict the HTTP methods allowed for views. Django will 
# throw an HTTP 405 (method not allowed) error if you try to access the view with any other HTTP method.
def post_comment(request, post_id):
    post = get_object_or_404(Post_Table, id = post_id, status = Post_Table.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST) # commentform is filled with the data from the user and form becomes an object the commentform is a class.
    # print(form)
    if form.is_valid(): 
        comment = form.save(commit=False) # create a comment object without saving it to the database

        comment.post_table = post # this would store the comment's id in the comment_table database
        # print(comment.post_table) # this will print the string representation in the model.py file of the comment_table
        comment.save()
    context = {
        'post': post,
        'form': form,
        'comment':comment
    }
    return render(request, 'blog/post/comment.html', context )

# def post_share(request, post_id):
#     post = get_object_or_404(Post_Table, pk = post_id, status = Post_Table.Status.PUBLISHED)
#     if request.method == 'GET':
#         form = EmailPostForm()
#         context = {
#             'form': form,
#             'post':post,
#         }
#         return render(request, 'blog/post/share.html', context)
    
#     elif request.method == 'POST':
#         try:
#             form = EmailPostForm(request.POST)
#             if form.is_valid():
#                 cd = form.cleaned_data

#         except Exception as e:
#             context['error'] = 'bad data'
#             return render(request, 'blog/post/share.html', context)