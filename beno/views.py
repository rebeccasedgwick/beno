from django.shortcuts import render
from beno.models import Task, Tag
from django.views import generic


def index(request):
    """View function for homepage of the site."""
    num_tasks = Task.objects.all().count()
    num_incomplete_tasks = Task.objects.filter(complete__exact='False').count()
    num_tags = Tag.objects.all().count

    context = {
        'num_tasks': num_tasks,
        'num_incomplete_tasks': num_incomplete_tasks,
        'num_tags': num_tags,
    }

    return render(request, 'index.html', context=context)


class TaskList(generic.ListView):
    queryset = Task.objects.filter(complete__exact='False')
    context_object_name = 'incomplete_task_list'
    template_name = 'tasks/incomplete_task_list.html'
