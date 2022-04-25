from datetime import datetime, timedelta, date
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm


class CalendarView(generic.ListView):
    model = Event
    template_name = 'timereg/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # call the formathmonth method, which returtns calendar as a table
        html_cal = cal.formatmonth(withyear=True)

        context = {
            'prev_month': prev_month(d),
            'next_month': next_month(d),
            'calendar': mark_safe(html_cal)
        }   
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event_new(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('timereg:calendar'))
    context = {
        'form': form
    }
    return render(request, 'timereg/event.html', context)

def event_edit(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'GET':
        form = EventForm(instance=event)
    else:
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'timereg/event.html', context)