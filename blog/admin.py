from django.contrib import admin
from .models import Post, Comment, Photo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at','updated_at','published')
    list_filter = ('published','created_at','updated_at')
    search_fields = ('title','content')




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','post','created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username','body')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploaded_at')