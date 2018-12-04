# Converts to JSON, validations ofr data passed
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
        read_only_fields = ['user']

    def validate_description(self, value):
        queryset = Task.objects.filter(description__iexact=value)
        # exclude current instance included if it exists already
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError("This task already exists")
        return value
