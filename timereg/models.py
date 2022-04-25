from datetime import datetime

from django.db import models
from django.urls import reverse
from .widget import *


class Event(models.Model):
    title = models.CharField(max_length=200, default="Czas pracy")
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def timeCout(self):
        time = datetime.combine(datetime(1,1,1,0,0,0), self.end_time) - datetime.combine(datetime(1,1,1,0,0,0), self.start_time)
        return time

    @property
    def get_html_url(self):
        time = self.timeCout()
        url = reverse('timereg:event_edit', args=(self.id,))
        return f'<a href="{url}"> {time} </a>'

    def __str__(self):
        return self.title