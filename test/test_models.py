from django.contrib.auth import get_user_model
from django.test import TestCase

from to_do_list.models import Tag, Task


class ModelTest(TestCase):

    def test_tag_str(self) -> None:
        tag_ = Tag.objects.create(
            name="others"
        )

        self.assertEqual(str(tag_), tag_.name)

    def test_task_create_with_elements(self):
        username = "user2"
        password = "user23456"
        person = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        task = Task.objects.create(
            description="Create TestTask1",
            deadline="2023-04-28",
            is_completed="False",
            owner=person
        )

        self.assertEqual(task.description, "Create TestTask1")
        self.assertEqual(task.deadline, "2023-04-28")
        self.assertEqual(task.is_completed, "False")
        self.assertEqual(task.owner.username, "user2")



