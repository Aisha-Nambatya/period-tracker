from django.contrib.auth.models import User
from django.db import models


class PeriodRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    flow_level = models.CharField(max_length=10)  # e.g., Light, Medium, Heavy
    symptoms = models.JSONField(default=list)  # Store symptom list
    moods = models.JSONField(default=list)  # Store mood list
    notes = models.TextField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
