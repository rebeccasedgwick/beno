from django.contrib import admin
from beno.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'user', 'due_by', 'priority', 'complete')
    list_filter = ('complete', 'priority', 'category', 'due_by')
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Task info', {
            'fields': ('description', 'notes', 'category')
        }),
        ('Prioritization', {
            'fields': ('priority', 'due_by')
        }),
        ('Status', {
            'fields': ('complete',)
        }),
    )


admin.site.register(Category)
