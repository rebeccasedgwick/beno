from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', views.TaskDetail.as_view(), name='task-detail'),
    path('tags/', views.TagList.as_view(), name='tags'),
]
