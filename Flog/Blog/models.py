from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    author =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save() 

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length = 255)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

''' class User(models.Model):
    name = models.CharField
    surname = 
    birthday =
    job =
    hobby = 
    bio =
'''

'''class Tag(models.Model):
    django-tagging
'''