from django import forms
from django.forms import ModelForm
from . models import Tasks

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Add in a new Tasks"}))

    class Meta:
        model = Tasks
        fields = '__all__'
