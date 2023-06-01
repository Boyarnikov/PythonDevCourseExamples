from django import forms
from . import models

class CreateNewTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ["name", "description"]
        widgets = {"name": forms.TextInput(),
                   "description": forms.TextInput(attrs={"class":"form-control"})}
        
    def change_widget(self):
        self.fields["description"].widget.attrs.update({"aria-describedby":"inputGroup-sizing-lg"})
    
class CreateNewTask1(forms.Form):
    class Meta:
        fields = ["name"]
    
    name = forms.CharField(max_length=100, label="New task name")
    description = forms.CharField(max_length=100, label="Task description")
