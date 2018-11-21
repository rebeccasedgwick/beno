from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_tasks/', views.AllTasksList.as_view(), name='all-tasks'),
    path('open_tasks/', views.OpenTasksList.as_view(), name='open-tasks'),
    path('task/<int:pk>', views.TaskDetail.as_view(), name='task-detail'),
    path('tags/', views.TagList.as_view(), name='tags'),
    path('tag/<int:pk>', views.TagDetail.as_view(), name='tag-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]
