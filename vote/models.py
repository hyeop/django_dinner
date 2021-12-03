from django.db import models
from acc.models import User

# Create your models here.
class Topic(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    pubdate = models.DateTimeField()
    content = models.TextField()
    voter = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.subject


class Choice(models.Model):
    subject = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="vote")
    comment = models.TextField()
    choicer = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"[{self.subject}] {self.name}"