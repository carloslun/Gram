from django.urls import path
from posts import views

urlpatterns = [
    path(
        route = '',
        view = views.FeedListView.as_view(),
        name = 'feed',
    ),
    path(
        route = 'posts/new/',
        view = views.PostCreateView.as_view(),
        name = 'create',
    ),
    path(
        route = 'posts/<pk>',
        view = views.PostDetailView.as_view(),
        name = 'post_detail'
    )
] 