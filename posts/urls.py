from django.urls import path
from . import views
from .views import PostListView, detailPostView, createPostView

urlpatterns = [
    path('post/', createPostView, name='posts-create'),
    path('', PostListView.as_view(), name='posts-home'),
    ]
