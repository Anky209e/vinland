from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser

class myUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username']

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'username', 'email']

