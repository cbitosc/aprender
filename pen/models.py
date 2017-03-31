from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(User)
    slug = models.SlugField(unique=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return "{}, {}".format(self.title, self.author.username)
