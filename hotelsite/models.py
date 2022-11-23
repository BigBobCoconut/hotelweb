from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

class Comment(models.Model):
    topic = models.ForeignKey(Topic, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
