from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import TaskForm
from catalog.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")


def toggle_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("catalog:task-list"))


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("catalog:tag-list")
