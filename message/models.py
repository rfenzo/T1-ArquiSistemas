from django.db import models
from django.utils import timezone

class Message(models.Model):
    message = models.TextField()
    ip = models.CharField(max_length=20)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'ip: {self.ip} | timestamp:{self.date_added}'

