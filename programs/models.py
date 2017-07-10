from django.db import models
from model_utils.models import TimeFramedModel, TimeStampedModel
from accounts.models import User


class Field(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Prequest(TimeStampedModel):
    field = models.ForeignKey(Field)
    pending = models.BooleanField(default=True)
    requester = models.ForeignKey(User)

    def __str__(self):
        return "Prequest on %s by %s" %(self.field, self.requester)


class Program(TimeFramedModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    in_progress = models.BooleanField(default=True)
    prequest = models.ForeignKey(Prequest, limit_choices_to={'pending': True})
    mentors = models.ManyToManyField(User,
                                     related_name='program_mentors',
                                     limit_choices_to={'groups__name': 'Mentor', 'is_verified': True})
    mentees = models.ManyToManyField(User,
                                     related_name='program_mentees',
                                     limit_choices_to={'groups__name': 'Mentee', 'is_verified': True})

    def __str__(self):
        return "Mentorship program (%s)" % self.title
