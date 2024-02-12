from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=20, default='light')
    layout = models.CharField(max_length=20, default='default')
    alarm_tone = models.CharField(max_length=100, default='default_alarm.mp3')

    class Meta:
        app_label = 'api'

class TravelHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    time_to_reach = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'api'
