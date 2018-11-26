import datetime

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from beno.models import Task, Category, User


@login_required
def index(request):
    """View function for homepage of the site."""
    num_tasks = Task.objects.filter(user=request.user.id).count()
    num_incomplete_tasks = Task.objects.filter(
        user=request.user.id,
        complete__exact='False'
        ).count()
    num_categories = Category.objects.filter(user=request.user.id).count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_tasks': num_tasks,
        'num_incomplete_tasks': num_incomplete_tasks,
        'num_categories': num_categories,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class AllTasksList(
        LoginRequiredMixin,
        generic.ListView
        ):
    context_object_name = 'all_tasks_list'
    template_name = 'beno/all_tasks_list.html'
    permission_required = 'task.can_mark_completed'

    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user
            ).order_by('due_by')


class OpenTasksList(
        LoginRequiredMixin,
        generic.ListView
        ):
    context_object_name = 'open_tasks_list'
    template_name = 'beno/open_tasks_list.html'
    permission_required = 'task.can_mark_completed'

    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user
            ).filter(
            complete__exact='False'
            ).order_by('due_by')


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class CategoryList(LoginRequiredMixin, generic.ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryDetail(LoginRequiredMixin, generic.DetailView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = [
        'description',
        'notes',
        'due_by',
        'complete',
        'priority',
        'category'
        ]
    default_due_date = datetime.datetime.now() + datetime.timedelta(days=7)
    initial = {'due_by': default_due_date}

    def form_valid(self, form):
        form.instance.user = User.objects.get(id=self.request.user.id)
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['description', 'notes', 'due_by', 'complete', 'category', 'priority']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('open-tasks')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', ]
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        form.instance.user = User.objects.get(id=self.request.user.id)
        return super(CategoryCreate, self).form_valid(form)


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categories')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'
