from tasks.models import List, Task

def test():
    l = List.objects.get(id=1)
    l.task_set.create(name = "task2", description = "second task")
    l.save()

    print("end_program")