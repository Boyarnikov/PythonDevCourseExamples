from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewTask
from . import models
from django.views.generic import ListView
from django.contrib.auth.models import User
import json
#from models import List, Task


def index(request):
    return render(request, "tasks/base.html")


def index_with_id(request, id):

    l = models.List.objects.get(id=id)
    
    print(l.parent, request.user)
    if l.parent != request.user:
        return redirect("http://127.0.0.1:8000/tasks/")
    if l:
        return render(request, "tasks/list.html", {"list":l, "const":42})

    return HttpResponse(f"<H1> НЕ НАЙДЕНО ПО ДАННОМУ ID</H1>")



def view_lists(request):
    if request.user.id == None:
        return redirect("http://127.0.0.1:8000/login")
        
    lists = request.user.list.all()

    class Data:
        l = None
        size = 0
        
        def __init__(self, size, l):
            self.size = size
            self.l = l
            
    lists = [Data(size = l.task_set.all().count(),  l=l) for l in lists]
    return render(request, "tasks/lists_view.html", {"lists":lists}) 


def rederect_to_list(request):
    return redirect("http://127.0.0.1:8000/tasks/")


def redact_task(request, id):
    l = models.List.objects.get(id=id)
    
    if request.method == "POST":
        
        for task in l.task_set.all():
            if request.POST.get("del"+str(task.id)) is not None:
                task.name = "[DELETED]"
                task.description = "[DELETED]"
                task.delete()
                l.save()
                return redirect("http://127.0.0.1:8000/tasks/"+str(l.id))
                
                
        
        t = CreateNewTask(request.POST)
        if t.is_valid():
            name = t.cleaned_data["name"]
            description = t.cleaned_data["description"]
            l.task_set.create(name=name, description=description)
            l.save()
            
    if l:
        t = CreateNewTask()
        return render(request, "tasks/list_redact.html", {"list":l, "new_task_form":t}) 
    

    return HttpResponse(f"<H1> НЕ НАЙДЕНО ПО ДАННОМУ ID</H1>")



def view_lists_search(request):
    if request.user.id == None:
        return redirect("http://127.0.0.1:8000/login")
        
    lists = request.user.list.all()

    class Data:
        l = None
        size = 0
        
        def __init__(self, size, l):
            self.size = size
            self.l = l
            
    lists = [Data(size = l.task_set.all().count(),  l=l) for l in lists]
    return render(request, "tasks/lists_view_with_search.html", {"lists":lists}) 


class SearchTasks(ListView):
    model = models.List
    template_name = "tasks/lists_view_with_search.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = self.request.user.list.all()
        context = super().get_context_data(**kwargs)
        
        lists = [{"name":d.name, "id":d.id, "size":d.task_set.all().count()} for d in data]
        context["qs_json"] = json.dumps(list(lists))
        print("===================================================")
        print(context)
        return context