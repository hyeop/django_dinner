from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    comment = models.TextField()
    point = models.IntegerField(default=0)
    pic = models.ImageField()

    def getpic(self):
        if self.pic:
            return self.pic.url
        else:
            return "/media/noimage.png"