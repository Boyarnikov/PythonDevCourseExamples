from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewTask
from . import models
#from models import List, Task

def index(request):
    return render(request, "tasks/base.html")


def index_with_id_with_string(request, id):
    s = ""
    q = models.List.objects.get(id=id)
    if q:
        s += f"<H1> INDEX PAGE WITH NUMBER {id}</H1>\n"
        s += f"<dir> {str(q)} </dir>" 
        return HttpResponse(s)
        
    return HttpResponse(f"<H1> НЕ НАЙДЕНО ПО ДАННОМУ ID</H1>")


def index_with_id(request, id):
    l = models.List.objects.get(id=id)
    if l:
        return render(request, "tasks/list.html", {"list":l, "const":42})
    

    return HttpResponse(f"<H1> НЕ НАЙДЕНО ПО ДАННОМУ ID</H1>")


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





def index_with_two_id(request, id, id2):
    return HttpResponse(f"<H1> INDEX PAGE WITH NUMBER {id} AND {id2}</H1>")