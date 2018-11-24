import datetime

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from beno.models import Task, Category


class TaskModelForm(ModelForm):
    def clean_data(self):
        data = self.cleaned_data

        # Check if a date is not in the past
        if data['due_by'] < datetime.date.today():
            raise ValidationError(_('Please enter a future date'))

        # Check if a date is in the allowed range (+6 months from now)
        if data['due_by'] > datetime.dateime.now() + datetime.timedelta(
            months=4
        ):
            raise ValidationError(_('Date must be less than 6 months away'))

        # Return the cleaned data
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
