from django.shortcuts import render
from datetime import date
from .models import Post

all_posts = Post.objects.order_by('-date')
latest_posts = Post.objects.all()[:3]


def starting_page(request):
  # sorted_posts= all_posts.sort(key=get_date)


  return render(request, "blog/index.html",{"data":latest_posts})

def posts(request):
  return render(request, "blog/all-posts.html",{
    "all_posts":all_posts
  })

def posts_detail(request, slug):
  identified_post = next(post for post in all_posts if post.slug == slug)
  return render(request, "blog/post-detail.html",{"post":identified_post})