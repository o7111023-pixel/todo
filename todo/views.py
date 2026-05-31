from django.shortcuts import render
from .models import Task, Tag


def task_list(request):
    tasks = Task.objects.prefetch_related("tags").all().order_by(
        "is_done", "-created_at"
    )
    return render(request, "todo/task_list.html", {"tasks": tasks})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "todo/tag_list.html", {"tags": tags})
