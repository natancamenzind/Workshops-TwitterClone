from django.conf import settings
from django.db import models


class Tweet(models.Model):

    content = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
