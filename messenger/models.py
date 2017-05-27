from django.db import models


# Create your models here.


class Message(models.Model):
    message_text = models.CharField(max_length=2000)
    sent = models.DateTimeField('Sent On')

    def __str__(self):
        return self.message_text
