from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    first_name = CharField(_("User firstname"), blank=True, max_length=30)
    last_name = CharField(_("User lastname"), blank=True, max_length=150)
    email = CharField(_("User email"), blank=True, max_length=254)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    class Meta:
        db_table = 'auth_user'


class Task(models.Model):
    """Model representing a task to do."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = CharField(
        'Task',
        max_length=300,
        help_text='Enter new task'
    )

    category = models.ManyToManyField(
        'Category',
        help_text='Select a category for this task',
        blank=True
    )
    due_by = models.DateTimeField()
    complete = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    PRIORITY = (
        ('1', '1 - High'),
        ('2', '2 - Medium'),
        ('3', '3 - Low')
    )

    priority = CharField(
        max_length=1,
        choices=PRIORITY,
        blank=False,
        default='2'
    )

    @property
    def is_overdue(self):
        if self.due_by and timezone.now() > self.due_by:
            return True
        return False

    def __str__(self):
        """String for representing the Model object"""
        return self.description

    def get_absolute_url(self):
        """Returns the url to access a detail record for this task"""
        return reverse('task_detail', args=[str(self.id)])

    class Meta:
        ordering = ['due_by', 'priority']


class Category(models.Model):
    """Model representing a category for a task (e.g. home, work, travel)"""
    name = CharField(max_length=200, help_text='Choose a category')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this category"""
        return reverse('category-detail', args=[str(self.id)])
