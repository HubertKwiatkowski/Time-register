from django.db import models
from django.urls import reverse
from .widget import *


class Event(models.Model):
    title = models.CharField(max_length=200, default="Czas pracy")
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    @property
    def get_html_url(self):
        url = reverse('timereg:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return self.title