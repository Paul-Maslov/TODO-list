from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from django.urls import reverse

from to_do_list.models import Task, Tag

TASK_URL = reverse("to_do_list:task-list")
TAG_URL = reverse("to_do_list:tag-list")

PAGINATION = 1


class PublicPostTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_task_list_login_required(self):
        res = self.client.get(TASK_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_tag_list_login_required(self):
        res = self.client.get(TAG_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivatePostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="user12345",
        )
        self.client.force_login(self.user)
        username = "test_user1"
        password = "user112345"
        self.person = get_user_model().objects.create_user(
            username=username,
            password=password
        )

    def test_task_list_response_with_correct_template(self):
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "to_do_list/task_list.html")

    def test_tag_list_response_with_correct_template(self):
        response = self.client.get(TAG_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "to_do_list/tag_list.html")

    def test_retrieve_tasks(self):
        self.task1 = Task.objects.create(
            description="Create TestTask1",
            deadline="2023-04-28",
            is_completed="False",
            owner=self.person
        )
        self.task2 = Task.objects.create(
            description="Create TestTask2",
            deadline="2023-04-29",
            is_completed="False",
            owner=self.person
        )
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task1.description)
        self.assertContains(response, self.task2.description)
        self.assertTemplateUsed(response, "to_do_list/task_list.html")

    def test_retrieve_tags(self):
        self.tag1 = Tag.objects.create(
            name="TestTag 1"
        )
        self.tag2 = Tag.objects.create(
            name="TestTag 2"
        )
        response = self.client.get(TAG_URL)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tag1.name)
        self.assertContains(response, self.tag2.name)
        self.assertTemplateUsed(response, "to_do_list/tag_list.html")

    def test_task_list_paginated_correctly(self):
        task_name = "Test Task 3"
        self.task = Task.objects.create(
            description=task_name,
            is_completed=False,
            owner=self.person
        )
        response = self.client.get(TASK_URL)

        self.assertEqual(len(response.context["task_list"]), PAGINATION)
