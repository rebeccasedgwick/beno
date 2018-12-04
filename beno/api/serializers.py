from rest_framework import serializers
from beno.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'pk',
            'user',
            'description',
            'notes',
            'category',
            'due_by',
            'complete',
            'priority',
        ]
