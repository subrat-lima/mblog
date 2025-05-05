from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class PostStatusChoice(models.TextChoices):
    DRAFT = "D"
    PUBLISHED = "P"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)
    content = models.TextField()
    status = models.CharField(
        max_length=1, choices=PostStatusChoice.choices, default=PostStatusChoice.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<{self.title}>"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
