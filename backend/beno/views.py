from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from beno.models import Task, Category
from beno.forms import SignUpForm

User = get_user_model()


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
