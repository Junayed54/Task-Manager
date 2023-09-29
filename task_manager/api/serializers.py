from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'created_at', 'updated_at', 'image']

class UserSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True)  # Include related tasks

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'task']


