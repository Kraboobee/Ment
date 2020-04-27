"""Module used for API.

This module will serialize the relevant classes and allow the user and doctor to get info in JSON format
"""

from rest_framework import serializers
from .models import Entry, Task

class EntrySerializer(serializers.ModelSerializer):
    """Serializes Entry to convert to JSON"""
    fields = ('user', 'date', 'mood')           # Should return all Entries where user==USER
    
    class Meta:
        model = Entry
        
        
class TaskSerializer(serializers.ModelSerializer):
    """Serializes Tasks"""
    fields = ('entry', 'title', 'done')          # Should return all tasks where user==USER and date==DATE
    
    class Meta:
        model = Task