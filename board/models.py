from django.db import models
from acc.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    content = models.TextField()
    pubdate = models.DateTimeField()
    likey = models.ManyToManyField(User, blank=True)

    def summary(self):
        if len(self.content) >= 15:
            return self.content[:15] + " ..."
        return self.content 

    def writerpic(self):
        u = User.objects.get(username=self.writer)
        return u.getpic()
        

class Reply(models.Model):
    sub = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=100)
    comment = models.TextField()

    def replyerpic(self):
        u = User.objects.get(username=self.replyer)
        return u.getpic()