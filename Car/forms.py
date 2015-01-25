__author__ = 'KATE'
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Comments
from testdrive.models import TestDrive

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['ctext']

class TestDriveForm(ModelForm):
    class Meta:
        model = TestDrive


class Registration(ModelForm):
    class Meta:
        model = User
