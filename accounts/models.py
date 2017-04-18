from django.contrib.auth.models import AbstractUser

TESTING_PASSWORD = 'password'


class User(AbstractUser):
    def __str__(self):
        return self.username
