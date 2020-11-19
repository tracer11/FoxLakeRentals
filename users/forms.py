from django.contrib.auth.forms import UserCreationFrom, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationFrom):
  class meta(UserCreationFrom):
    model = CustomUser
    fields = ['email', 'phone', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
  class meta(UserChangeForm):
    model = CustomUser
    fields = ['email', 'phone']
