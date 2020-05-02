"""Module used for API.

This module will serialize the relevant classes and allow the user and doctor to get info in JSON format
"""

from rest_framework import serializers
from tracker.models import Entry, CommitMent

class EntrySerializer(serializers.ModelSerializer):
    """Serializes Entry to convert to JSON"""
    
    class Meta:
        model = Entry
        fields = ('user', 'date', 'mood')           # Should return all Entries where user==USER
        
        
# class TaskSerializer(serializers.ModelSerializer):
#     """Serializes Tasks"""
#     fields = ('entry', 'title', 'done')          # Should return all tasks where user==USER and date==DATE
    
#     class Meta:
#         model = CommitMent