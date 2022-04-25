from django.urls import path

from . import views

app_name = 'timereg'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
]