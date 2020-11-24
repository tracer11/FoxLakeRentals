from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, PostImage 
from .forms import FullPostForm
from django.contrib import messages

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'

def detailPostView(request, id):
  post = get_object_or_404(Post, id)
  photos = PostImage.objects.filter(post=post)
  return render(request, 'post-detail', {'photos':photos, 'post':post})

def createPostView(request):
  if request.method == 'POST':
    form = FullPostForm(request.POST, request.FILES)
    files = request.FILES.getlist('images')
    if form.is_valid():
      user = request.user
      title = form.cleaned_data.get('title')
      description = form.cleaned_data.get('description')
      rate = form.cleaned_data.get('rate')
      post_obj = Post.objects.create(title=title, description=description, rate=rate, posted_by=user)
      for f in files:
        PostImage.objects.create(post=post_obj, image=f)
    else:
      messages.error('Form is Invalid')




