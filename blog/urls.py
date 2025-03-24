from django.urls import path
from . import views

app_name = 'blog' # this allows you to organize URLs by application and use the name when referring to them.
urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name = 'post_list'),
    path('<int:id>/<slug:slug>/', views.post_detail, name='post_detail'),
    #path('<int:id>/', views.post_detail, name='post_detail'),
    # path('<int:post_id>/', views.post_share, name='post_share'),
    path('<int:post_id>/comment', views.post_comment, name='post_commentt')
]