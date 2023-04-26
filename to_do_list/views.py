from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from to_do_list.models import Task, Tag


def change_task_status(request, pk):
    if 'dobtn' in request.POST:
        profil = get_object_or_404(Task, id=pk)
        if profil.is_completed:
            profil.is_completed = False
        else:
            profil.is_completed = True
        profil.save(update_fields=["is_completed"])
    return redirect('to_do_list:task-list')


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    success_url = reverse_lazy("to_do_list:task-list")
    context_object_name = "task_list"
    paginate_by = 5


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:task-list")
    template_name = "to_do_list/task_form.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:task-list")
    template_name = "to_do_list/task_form.html"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "to_do_list/task_confirm_delete.html"
    success_url = reverse_lazy("to_do_list:task-list")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    success_url = reverse_lazy("to_do_list:tag-list")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("to_do_list:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("to_do_list:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    template_name = "to_do_list/tag_confirm_delete.html"
    success_url = reverse_lazy("to_do_list:tag-list")
