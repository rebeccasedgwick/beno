from rest_framework import generics
from beno.models import Task
from .serializers import TaskSerializer


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()
