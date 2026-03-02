from importlib.resources import contents

from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def edit(self, title, content, image, author, tag, edited_date):
        self.edited_date = timezone.now()
        self.title = title
        self.content = content
        self.image = image
        self.author = author
        self.tag = tag
        self.save()

    def description(self):
        if len(self.content) > 500:
            return self.content[:500]
        else:
            return self.content


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, blank=True)
    bio = models.TextField(verbose_name="Persona Summary", max_length=300, blank=True)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cv_file = models.FileField(upload_to='cvs/', null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    social_links = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.nickname}"
