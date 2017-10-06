from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Member(TimeStampedModel):
    email = models.TextField(default="")
    name = models.TextField(default="")
    password = models.TextField(default="")

    def __str__(self):
        return self.email