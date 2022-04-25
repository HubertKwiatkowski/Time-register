from django import forms
from django.conf import settings
from django.template.loader import render_to_string

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'