from django.urls import path

from . import views

app_name = 'timereg'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event_new, name='event_new'),
    path('event/<int:event_id>/edit/', views.event_edit, name='event_edit'),
]