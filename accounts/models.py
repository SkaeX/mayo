from django.contrib.auth.models import AbstractUser
from django.db import models

TESTING_PASSWORD = 'password'


class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        groups = self.groups.all()
        group_str = ''
        for group in groups:
            group_str += group.name + '|'

        return '[%s] %s' % (group_str, self.email)
