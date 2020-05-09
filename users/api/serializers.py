"""Model used for User API.

This model will be used to serialize the user's personal information. 
This includes information relating to the user's prescribed medications, and the habits and hobbies the 
user has decided to track.
"""

from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Profile, TreatMent, FulfilMent

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'Treatment', 'Fulfilment')
    
    

# TODO
    # API for USER
    # name
    # medication
    # habits