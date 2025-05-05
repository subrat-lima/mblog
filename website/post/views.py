from django.http import Http404
from django.shortcuts import get_object_or_404, render

from post.models import Post, PostStatusChoice


def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.status != PostStatusChoice.PUBLISHED:
        raise Http404("Post does not exist")
    return render(request, "post/view_post.html", {"post": post})
