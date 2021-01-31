from django.urls import path
from .views import create_task, task_view

urlpatterns = [
path("", create_task, name="create_task"),
path("/tasks/", task_view, name="task_view")

]