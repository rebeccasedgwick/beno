from django.urls import path
from .views import (
    TaskRetrieveUpdateDestroyView,
    TaskCreateView,
    TaskListView,
    TaskUncompletedListView,
)

urlpatterns = [
    path('task/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('all_tasks/', TaskListView.as_view(), name='all-tasks'),
    path('open_tasks/', TaskUncompletedListView.as_view(), name='open-tasks'),
]
