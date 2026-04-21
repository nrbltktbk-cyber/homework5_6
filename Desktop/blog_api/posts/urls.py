from django.urls import path
from .views import PostViewSet, CommentViewSet

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('posts/', post_list),
    path('posts/<int:pk>/', post_detail),
    path('posts/<int:post_id>/comments/', comment_list),
]