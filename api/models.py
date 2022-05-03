from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=255, blank=False, null=False)
    contents = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

