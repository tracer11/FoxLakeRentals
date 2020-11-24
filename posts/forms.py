from django import forms 
from .models import Post, PostImage

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'description', 'rate']

class FullPostForm(PostForm):
  images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

  class Meta(PostForm.Meta):
    fields = PostForm.Meta.fields + ['images']
