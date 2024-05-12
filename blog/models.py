from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
  first_name = models.CharField(max_length=50);
  last_name = models.CharField(max_length=50)
  email = models.EmailField()
  
  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
class Post(models.Model):
  title = models.CharField(max_length=100)
  excerpt = models.TextField()
  image = models.CharField(max_length=50, blank=True)
  date = models.DateField()
  slug = models.SlugField(default="",null=False, blank=True)
  content = models.TextField()
  author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
  
  
  def get_absolute_url(self):
    return reverse("post-detail-page", args=[self.slug])
  
  def __str__(self):
    return f"{self.title} {self.excerpt}"
  


class Tag(models.Model):
  caption = models.CharField(max_length=50)
  tag = models.ManyToManyField(Post, related_name="post")
  
  def __str__(self):
    return f"{self.caption}"
