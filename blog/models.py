from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    """Represents a single blog post."""
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True, blank=True)  # URL-friendly title
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content     = CKEditor5Field('Content', config_name='extends')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    published   = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self):
        # Auto-generate slug from title
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Comment(models.Model):
    """Represents a comment on a blog post."""
    post       = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body       = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on '{self.post.title}'"

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

class Videos(models.Model):
    video = models.FileField(upload_to = 'videos/')
    title = models.TextField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
