from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxSelectMultiple
from django.forms import ModelForm

from .models import Profile
from .models import User


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'schools', 'degrees', 'program', 'grad_year',
            'resume', 'searchable'
        ]
        widgets = {
            'schools': CheckboxSelectMultiple(),
            'degrees': CheckboxSelectMultiple(),
        }

# http://disq.us/p/1qc62i7
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email", "password1", "password2"
        )
