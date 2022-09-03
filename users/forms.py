from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
    def save(self, commit = True):
        user = super(SignupForm, self).save(commit=False)
        if commit:
            user.save()
        return user
