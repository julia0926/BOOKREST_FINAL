from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from .models import CustomUser, UserManager
from .choices import *

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    # 사용자 생성 폼
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2", "username", "major", "student_id", "phone_number")
