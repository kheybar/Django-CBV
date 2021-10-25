from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title