# Converts to JSON, validations of data passed
from rest_framework import serializers
from beno.models import Task, Category


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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name', 'user', ]
        read_only_fields = ['user']

    def validate_description(self, value):
        queryset = Category.objects.filter(description__iexact=value)
        # exclude current instance included if it exists already
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError("This category already exists")
        return value
