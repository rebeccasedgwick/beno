from django.urls import path
from .views import TaskRetrieveUpdateDestroyView, TaskCreateView, TaskListView


urlpatterns = [
    path('task/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('all_tasks/', TaskListView.as_view(), name='all-tasks'),

]
