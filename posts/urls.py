from django.urls import path
from . import views
from .views import PostListView, detailPostView

urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),
    ]
