from .models import Todo
from rest_framework import serializers
# from rest_framework import viewsets, permissions
# from .serializers import TodoSerializer

# Class TodoSerializer is a subclass of serializers.HyperlinkedModelSerializer.
# For serializing and deserializing data into representations such as json.

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # Meta class is for configuring the TodoSerializer class
    class Meta:
        # Model to serialize
        model = Todo

        # Fields to show in json
        fields = ('id', 'subject', 'details')