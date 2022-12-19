from django.db import models
from PIL import Image 
from django.utils import timezone
from django.conf import settings

from core.accounts.models import CustomUser

class Event(models.Model):
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # auto_add_now = makes field efitable on admin field
    # auto_now =  inherit editable=False

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamp'''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()

    #     return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Submission(models.Model):
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='submissions')
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    detail = models.TextField(null=True, blank=True)


    def __str__(self):
        return f" {str(self.event)} {str(self.participant)}"
        
