from rest_framework import generics, filters
from beno.models import Task
from .serializers import TaskSerializer


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self):
        current_user = self.request.user
        return Task.objects.filter(user=current_user)


class TaskCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('due_by', 'priority')
    ordering = ('due_by', 'priority',)

    def get_queryset(self):
        """
        This view returns a detail view of a Task for the current
        authenticated user, with default ordering of soonest due &
        highest priority first.
        """
        current_user = self.request.user
        return Task.objects.filter(user=current_user)
