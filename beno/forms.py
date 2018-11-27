import datetime
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from beno.models import Task, Category


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
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.'
        )
    last_name = forms.CharField(
        max_length=150, required=False, help_text='Optional.'
        )
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.'
        )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            )
