import datetime
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from beno.models import Task, Category, User


class TaskModelForm(ModelForm):
    def clean_data(self):
        data = self.cleaned_data

        if data['due_by'] < datetime.date.today():
            raise ValidationError(_('Please enter a future date'))

        if data['due_by'] > datetime.datetime.now() + datetime.timedelta(
            months=4
        ):
            raise ValidationError(_('Date must be less than 6 months away'))

        return data

    class Meta:
        model = Task
        fields = '__all__'


class CategoryModelForm(ModelForm):
    def clean_data(self):
        data = self.cleaned_data

        return data

    class Meta:
        model = Category
        fields = '__all__'


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'name')
