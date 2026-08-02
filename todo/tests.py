from django.test import TestCase

from todo.models import Tag, Task


class TagModelTest(TestCase):
    def test_str(self):
        tag = Tag.objects.create(name="Work")

        self.assertEqual(str(tag), "Work")


class TaskModelTest(TestCase):
    def test_str(self):
        task = Task.objects.create(content="Learn Django")

        self.assertEqual(str(task), "Learn Django")
