from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    owner = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('timereg:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return self.title