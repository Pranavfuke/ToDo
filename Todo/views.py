from django.shortcuts import render
from ToDoApp.models import Task

def Home(request):

    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks' : tasks
    }
    return render(request , 'home.html' , context)