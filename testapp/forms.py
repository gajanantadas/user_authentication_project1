from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','is_staff','is_active']
        labels={'email':'Email'}
class EditUserForm(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields= ['username','first_name','email','last_name','is_active','is_staff']
        labels={'email':'Email'}
class EditAdminForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email':'Email'}

