from django.conf import settings
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password):
        user = self.model(email=email, name=name, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email=email, name=name, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("Full name"), blank=True, max_length=60)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['name', 'password']
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def get_short_name(self):
        return self.name

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email


class Task(models.Model):
    """Model representing a task to do."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(
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

    priority = models.CharField(
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
    name = models.CharField(max_length=200, help_text='Choose a category')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this category"""
        return reverse('category-detail', args=[str(self.id)])
