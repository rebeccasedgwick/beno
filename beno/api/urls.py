from django.urls import path
from .views import TaskRetrieveUpdateDestroyView, TaskCreateView


urlpatterns = [
    path('task/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create')
]
