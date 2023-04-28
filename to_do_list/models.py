from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(AbstractUser):

    class Meta:
        ordering = ["username"]


class Task(models.Model):
    description = models.TextField(default="Add the task description!")
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(default="2000-01-01")
    is_completed = models.BooleanField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="task",
    )
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_completed", "deadline"]
