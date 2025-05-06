from django.contrib import admin

from posts.models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "slug", "author", "publish", "title", "status")
    ordering = ["status", "publish"]
    raw_id_fields = ["author"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "user", "post", "body")
    raw_id_fields = ["user"]
