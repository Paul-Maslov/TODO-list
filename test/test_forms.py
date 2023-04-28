from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from to_do_list.models import Tag, Task


class TaskFormsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user2",
            password="user23456",
        )
        self.client.force_login(self.user)

        self.tag1 = Tag.objects.create(name="home")
        self.tag2 = Tag.objects.create(name="shop")

    def test_create_task(self):
        task_name = "Test create Task"
        response = self.client.post(
            reverse(
                "to_do_list:task-create"
            ),
            {
                "description": task_name,
                "is_completed": "False",
                "deadline": "2023-04-15",
                "owner": self.user.id,
                "tags": [self.tag1.id, ]
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.get(id=11).description, "Test create Task")

    def test_update_task(self):
        task_name = "Test create Task"
        task = Task.objects.create(
            description=task_name,
            deadline="2023-04-15",
            is_completed=False,
            owner=self.user,
         )
        task.tags.set([self.tag1.id, ])

        response = self.client.post(
            reverse(
                "to_do_list:task-update",
                kwargs={"pk": task.id}
            ),
            {
                "pk": task.id,
                "description": "Try to update Task",
                "deadline": "2023-04-15",
                "is_completed": "False",
                "owner": self.user.id,
                "tags": self.tag1.id
            },
        )

        Task.objects.get(id=task.id).refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.get(id=task.id).description, "Try to update Task")

    def test_delete_task(self):
        task_name = "Test delete Task"
        task = Task.objects.create(
            description=task_name,
            is_completed=False,
            owner=self.user
        )
        task.tags.set([self.tag1.id, ])
        response = self.client.post(
                reverse("to_do_list:task-delete", kwargs={"pk": task.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
