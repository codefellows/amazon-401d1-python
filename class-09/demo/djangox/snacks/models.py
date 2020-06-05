from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    eater = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
