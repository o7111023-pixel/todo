from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Task, Tag


# ---------------- TASK ----------------

class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.prefetch_related("tags").order_by("is_done", "-created_at")


class TaskCreateView(CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["content", "deadline", "tags", "is_done"]
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:task-list")


# ---------------- TAG ----------------

class TagListView(ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")
