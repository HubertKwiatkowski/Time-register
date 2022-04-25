from django import forms
from django.forms import ModelForm, DateInput

from .widget import DatePickerInput, TimePickerInput
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        # widgets = {
        #     'start_time': DateInput(
        #         attrs={'type': 'datetime-local'},
        #         format='%Y-%m-%dT%h:%M'
        #         ),
        #     'end_time': DateInput(
        #         attrs={'type': 'datetime-local'},
        #         format='%Y-%m-%dT%h:%M'
        #         )
        # }
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

    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, *kwargs)
    #     # input_formats to parse HTML5 datetime-local input to datetime field
    #     self.fields['start_time'].input_formats = ('%Y-%m-%dT%h:%M',)
    #     self.fields['end_time'].input_formats = ('%Y-%m-%dT%h:%M',)