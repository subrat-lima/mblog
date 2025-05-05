from django.urls import path

from post import views

urlpatterns = [
    path("<int:post_id>/", views.view_post, name="view_post"),
]
