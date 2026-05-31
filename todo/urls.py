from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("tags/", views.tag_list, name="tag-list"),
]
