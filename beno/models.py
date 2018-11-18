from django.db import models
from django.urls import reverse
import datetime


class Task(models.Model):
    """Model representing a task to do."""
    description = models.CharField(
        'Task',
        max_length=300,
        help_text='Enter new task'
    )

    tag = models.ManyToManyField(
        'Tag',
        help_text='Select a tag for this task',
        blank=True
    )
    due_by = models.DateTimeField()
    complete = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_by and datetime.datetime.now() > self.due_by:
            return True
        return False

    PRIORITY = (
        ('1', '1 - High'),
        ('2', '2 - Medium'),
        ('3', '3 - Low')
    )

    priority = models.CharField(
        max_length=1,
        choices=PRIORITY,
        blank=False,
        default='2'
    )

    class Meta:
        ordering = ['due_by', 'priority']

    def __str__(self):
        """String for representing the Model object"""
        return self.description

    def get_absolute_url(self):
        """Returns the url to access a detail record for this task"""
        return reverse('task-detail', args=[str(self.id)])


class Tag(models.Model):
    """Model representing a tag for a task (e.g. home, work, travel)"""
    name = models.CharField(max_length=200, help_text='Choose a tag')

    def __str__(self):
        """String for representing the Model object"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this tag"""
        return reverse('tag-detail', args=[str(self.id)])
