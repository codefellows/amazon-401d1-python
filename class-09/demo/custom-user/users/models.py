from django.contrib.auth.models import AbstractUser
from django.db import models # why????


class CustomUser(AbstractUser):
    pass # do we need this???

    # door left open for additional fields
    # e.g. Social Security
    # date of birth
    favorite_color = models.CharField(max_length=64, default="green")

    def __str__(self):
        return self.username

