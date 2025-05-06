from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from posts.forms import CommentForm
from posts.models import Post


def view_posts(request):
    posts = Post.published.all()
    return render(request, "post/view_posts.html", {"posts": posts})


def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(
        request,
        "post/view_post.html",
        {"post": post, "form": form, "comments": comments},
    )


@login_required
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
    return redirect("view_post", post_id=post.id)
