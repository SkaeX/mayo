from django.db import models
from accounts.models import User


class Field(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Request(models.Model):
    field = models.ForeignKey(Field)
    pending = models.BooleanField(default=True)
    mentee = models.ForeignKey(User)

    def __str__(self):
        return "Request on %s by %s" %(self.field, self.mentee)


class Program(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    in_progress = models.BooleanField(default=True)
    request = models.ForeignKey(Request)
    mentors = models.ManyToManyField(User, related_name='program_mentors')
    mentees = models.ManyToManyField(User, related_name='program_mentees')
