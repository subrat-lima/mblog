from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "author", "title", "status")
    raw_id_fields = ["author"]
