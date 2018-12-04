from django.urls import path
from .views import (
    TaskRetrieveUpdateDestroyView,
    TaskCreateView,
    TaskListView,
    TaskUncompletedListView,
    CategoryRetrieveUpdateDestroyView,
    CategoryCreateView,
    CategoryListView,
)

urlpatterns = [
    path('task/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('all_tasks/', TaskListView.as_view(), name='all-tasks'),
    path('open_tasks/', TaskUncompletedListView.as_view(), name='open-tasks'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
]
