from django.urls import path

from to_do_list.views import (
    TaskListView, TagListView,
    TaskCreateView, TaskUpdateView, TaskDeleteView,
    TagCreateView, TagUpdateView, TagDeleteView,
    change_task_status,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task-apply/<int:pk>/", change_task_status, name="change-status")

]

app_name = "to_do_list"
