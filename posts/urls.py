from django.urls import path
from . import views
from .views import PostListView, createPostView, detailPostView

urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),
    path('create/', createPostView, name='posts-create')
]
