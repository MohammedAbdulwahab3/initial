from django.urls import path
from .views import TaskAdd, TaskDelete, TaskEdit, TaskList

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/add/', TaskAdd.as_view(), name='task-add'),
    path('tasks/<int:pk>/', TaskEdit.as_view(), name='task-edit'),  # For editing tasks
    path('tasks/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
]
