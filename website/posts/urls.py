from django.urls import path

from posts import views

urlpatterns = [
    path("", views.view_posts, name="view_posts"),
    path("<int:post_id>/", views.view_post, name="view_post"),
    path("<int:post_id>/comment/", views.post_comment, name="post_comment"),
]
