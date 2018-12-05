from django.contrib.auth.forms import UserCreationForm

from beno.models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'name')
