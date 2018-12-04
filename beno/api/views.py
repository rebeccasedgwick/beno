from rest_framework import generics, filters
from beno.models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self):
        current_user = self.request.user
        return Task.objects.filter(user=current_user)


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListView(generics.ListAPIView):
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


class TaskUncompletedListView(TaskListView):
    def get_queryset(self):
        current_user = self.request.user
        return Task.objects.filter(user=current_user).filter(complete=False)


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer

    def get_queryset(self):
        current_user = self.request.user
        return Category.objects.filter(user=current_user)


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        current_user = self.request.user
        return Category.objects.filter(user=current_user)
