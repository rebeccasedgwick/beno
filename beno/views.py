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


class AllTasksList(LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('due_by')
    context_object_name = 'all_tasks_list'
    template_name = 'beno/all_tasks_list.html'


class OpenTasksList(LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).filter(complete__exact='False').order_by('due_by')
    context_object_name = 'open_tasks_list'
    template_name = 'beno/open_tasks_list.html'


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = Task


class TagList(LoginRequiredMixin, generic.ListView):
    model = Tag


class TagDetail(LoginRequiredMixin, generic.DetailView):
    model = Tag
