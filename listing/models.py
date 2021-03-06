from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    post_type = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    date_published = models.DateTimeField(auto_now=True)
    submitted_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
