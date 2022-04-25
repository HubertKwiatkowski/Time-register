from django import forms

from .widget import DatePickerInput, TimePickerInput
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    date = forms.DateField(
        widget=DatePickerInput
    )

    start_time = forms.TimeField(
        widget=TimePickerInput
    )
    end_time = forms.TimeField(
        widget=TimePickerInput
    )