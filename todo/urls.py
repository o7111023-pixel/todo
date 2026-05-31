from django.urls import path
from . import views
from .views import TaskCreateView

app_name = "todo"

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("tags/", views.tag_list, name="tag-list"),

    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/toggle/", views.task_toggle, name="task-toggle"),

    path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),
]
