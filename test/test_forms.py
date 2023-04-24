from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from to_do_list.models import Tag, Task


class TaskFormsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Paul",
            password="user12345",
        )
        self.client.force_login(self.user)

        username = "test_user1"
        password = "user112345"
        self.person = get_user_model().objects.create_user(
            username=username,
            password=password,
        )
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
                "owner": self.user.id,
                "tags": [self.tag1.id, ]
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.get(id=1).description, "Test create Task")

    def test_update_task(self):
        task_name = "Test create Task"
        task = Task.objects.create(
            description=task_name,
            is_completed=False,
            owner=self.person,
         )

        response = self.client.post(
            reverse(
                "to_do_list:task-update",
                kwargs={"pk": task.id}
            ),
            {
                "pk": task.id,
                "description": "Try to update Task",
                "is_completed": "False",
                "owner": self.person.id,
                "tags": [self.tag1.id, ]
            },
        )
        task.tags.set([self.tag2.id, ])
        Task.objects.get(id=task.id).refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.get(id=task.id).description, "Try to update Task")

    def test_delete_task(self):
        task_name = "Test delete Task"
        task = Task.objects.create(
            description=task_name,
            is_completed=False,
            owner=self.person
        )
        task.tags.set([self.tag1.id, ])
        response = self.client.post(
                reverse("to_do_list:task-delete", kwargs={"pk": task.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
