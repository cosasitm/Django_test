from django.contrib import admin
from .models import Author, Tag, Post

class adminPost(admin.ModelAdmin):
  prepopulated_fields = {'slug':('title',)}
  list_filter = ('author','tag','date')
  list_display = ("title","author")

# Register your models here.
admin.site.register(Author)

admin.site.register(Tag)
admin.site.register(Post, adminPost)
