from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="list")
    
    def __str__(self):
        return f"Task list {self.name} with {self.task_set.all()}"
    
    
    def get_name(self):
        return self.name
    
    
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    parent = models.ForeignKey(List, on_delete=models.CASCADE)
    
    def get_disr(self):
        return self.description
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return f"Task {self.name} from a list {self.parent.get_name()}" 