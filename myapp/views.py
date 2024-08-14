from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Welcome to Django Course'
    return render(request,'index.html', {
        'title': title
    })

def hello(request, username):
    return HttpResponse("Hello word %s"% username )

def about(request):
    username = 'Alfredo'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects/projects.html', {
        'projects': projects
    })

def task(request):
    # task = get_object_or_404(Task, title=title)
    tasks = Task.objects.all()
    return render(request,'tasks/task.html',{
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
       return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()
    })
    else:
        Task.objects.create(
            title       = request.POST['title'], 
            description = request.POST['description'], 
            project_id  =3
            )
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
         return render(request, 'projects/create_projects.html', {
        'form': CreateNewProject()
    })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')

   











