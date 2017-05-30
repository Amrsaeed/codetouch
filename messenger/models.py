from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):
    message_text = models.CharField(max_length=2000)
    sentOn = models.DateTimeField('Sent On')
    sender = models.CharField(max_length=150, default='None')
    reciever = models.CharField(max_length=150, default='None')

    def __str__(self):
        return self.message_text
