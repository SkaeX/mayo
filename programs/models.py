from django.db import models
from accounts.models import User


class Field(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class Request(models.Model):
    field = models.ForeignKey(Field)
    pending = models.BooleanField(default=True)
    mentee = models.ForeignKey(User)


class Program(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    in_progress = models.BooleanField(default=True)
    field = models.ForeignKey(Field)
    mentors = models.ManyToManyField(User)
    mentees = models.ManyToManyField(User)
