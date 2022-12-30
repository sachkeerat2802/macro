from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, WeightLog


class RegisterUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'animated-input'})
            field.required = True


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'name', 'email',
                  'location', 'metric', 'calorie_goal']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'edit-input'})


class WeightLogForm(ModelForm):
    class Meta:
        model = WeightLog
        fields = ['weight', 'entry_date']
        widgets = {
            'entry_date': forms.DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(WeightLogForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'edit-input'})
