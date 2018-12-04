from rest_framework import generics
from beno.models import Task
from .serializers import TaskSerializer


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()


class TaskCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
