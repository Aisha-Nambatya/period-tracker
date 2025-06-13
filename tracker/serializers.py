# tracker/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, PeriodRecord

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'birthday', 'average_cycle_length', 'average_period_length', 'last_period_start']

class PeriodRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodRecord
        fields = '__all__'
        read_only_fields = ['profile']
