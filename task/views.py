from django.shortcuts import render,  redirect
from django.http import HttpResponse
from . models import *
from . forms import *
# Create your views here.

# Create Task Start
def index(request):
    tasks = TaskModel.objects.all()
    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    

    context = {'tasks':tasks, 'form':form}

    return render(request, 'tasks/list.html', context)
# Create Task end


#Update Task Start
def UpdateTask(request, pk):
    task = TaskModel.objects.get(id=pk)

    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')    

    context = {'form':form}

    return render(request , 'tasks/Update_task.html', context)
#Update Task End

