from django import forms
from django.forms import fields
from .models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__' 