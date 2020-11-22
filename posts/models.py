from django.db import models
from django.conf import settings 
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=250)
  description = models.TextField()
  available = models.BooleanField(default=True)
  rate = models.IntegerField()
  posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Image(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="media/post_images")

