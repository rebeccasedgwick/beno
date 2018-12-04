from .views import TaskRetrieveUpdateDestroyView
from django.urls import path


urlpatterns = [
    path('task/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail')
]
