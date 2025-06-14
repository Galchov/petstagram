from django.contrib import admin

from .models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'photo']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['photo']
