from django import forms

class CreateNewTask(forms.Form):
    name = forms.CharField(max_length=100, label="New task name")
    description = forms.CharField(max_length=100, label="Task description")
