from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
