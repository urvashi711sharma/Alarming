# api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, TravelHistory

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['theme', 'layout', 'alarm_tone']

class TravelHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelHistory
        fields = ['destination', 'time_to_reach', 'timestamp']
