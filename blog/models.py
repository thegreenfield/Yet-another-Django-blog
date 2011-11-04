from django.db import models
import unidecode
import re

class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def save(self):
        self.slug = re.compile("[^a-zA-Z0-9_]+").sub("-", unidecode.unidecode(self.title.lower()))
        super(Post, self).save()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode(u"%s: %s" % (self.post, self.body[:60]))


