from django.contrib import admin
from beno.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'due_by', 'priority', 'complete')
    list_filter = ('complete', 'priority', 'tag', 'due_by')
    fieldsets = (
        ('Task info', {
            'fields': ('description', 'notes', 'tag')
        }),
        ('Prioritization', {
            'fields': ('priority', 'due_by')
        }),
        ('Status', {
            'fields': ('complete',)
        }),
    )
