from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_tasks/', views.AllTasksList.as_view(), name='all-tasks'),
    path('open_tasks/', views.OpenTasksList.as_view(), name='open-tasks'),
    # path('task/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
    # path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    # path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    # path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
]
