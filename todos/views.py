from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    # queryset is a list of all Todo objects
    queryset = Todo.objects.all()

    # The serializer_class attribute is used to control which serializer class should be used
    # for serializing and deserializing queryset and model instances.
    serializer_class = TodoSerializer

    # Set permission_classes to allow unrestricted access to the API
    permission_classes = [permissions.AllowAny]