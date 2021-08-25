from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Application


class CreateApplicantForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
        widgets = {"applicant": forms.HiddenInput(),
                   "jobs": forms.HiddenInput()
                   }
