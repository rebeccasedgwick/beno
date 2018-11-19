from django.shortcuts import render
from beno.models import Task, Tag
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    """View function for homepage of the site."""
    num_tasks = Task.objects.all().count()
    num_incomplete_tasks = Task.objects.filter(complete__exact='False').count()
    num_tags = Tag.objects.all().count
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_tasks': num_tasks,
        'num_incomplete_tasks': num_incomplete_tasks,
        'num_tags': num_tags,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class TaskList(LoginRequiredMixin, generic.ListView):
    queryset = Task.objects.filter(complete__exact='False')
    context_object_name = 'incomplete_task_list'
    template_name = 'beno/incomplete_task_list.html'


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = Task


class TagList(LoginRequiredMixin, generic.ListView):
    model = Tag


class TagDetail(LoginRequiredMixin, generic.DetailView):
    model = Tag
