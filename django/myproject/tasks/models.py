from django.db import models


class List(models.Model):
    name = models.CharField(max_length=100)
    
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