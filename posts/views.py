from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.contrib import messages
from .models import Post, PostImage
from .forms import PostForm, PostImageForm

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'

def detailPostView(request, id):
  post = get_object_or_404(Post, id)
  photos = PostImage.objects.filter(post=post)
  return render(request, 'post-detail', {'photos':photos, 'post':post})

@login_required
def createPostView(request):

  ImageFormSet = modelformset_factory(PostImage, form=PostImageForm, extra=5)

  if request.method == 'POST':
    postForm = PostForm(request.POST)
    formset = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())

    if postForm.is_valid() and formset.is_valid():
      post_form = postForm.save(commit=False)
      post_form.posted_by = request.user
      post_form.save()

      for form in formset.cleaned_data:
        if form:
          image = form['image']
          photo = PostImage(post=post_form, image=image)
          photo.save()
      messages.success(request, "Posting crated!")
      return redirect('posts-home')

    else:
      messages.error(postForm.errors, formset.errors)
  else:
    postForm = PostForm()
    formset = ImageFormSet(queryset=PostImage.objects.none())

  return render(request, 'posts/post_create.html', {'postForm':postForm, 'formset':formset})






