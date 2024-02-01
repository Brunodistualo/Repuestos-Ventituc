from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse
from .models import Project, Task,Ventiladores
from django.db.models import Q
from .forms import CreateNewProjectForm, CreateNewTaskForm
from django.contrib import messages

def projects(request):
    busqueda = request.GET.get("buscar")
    modelos = Project.objects.all()
    
    if busqueda:
        modelos = Project.objects.filter(
        Q(name__icontains = busqueda) | 
        Q(description__icontains = busqueda)
    ).distinct()
    return render(request, 'projects/projects.html', {'modelos': modelos})

def task(request):
    tasks = Task.objects.all()
    busqueda_2 = request.GET.get("buscar")
    if busqueda_2:
        tasks = Task.objects.filter(
            Q(title__icontains = busqueda_2) |
            Q(description__icontains = busqueda_2) |
            Q(modelo_vt__icontains = busqueda_2)
        ).distinct()
    return render(request, 'task/task.html',{
        'tasks':tasks,
        })
          
def ventilador_search(request):
    resultados_vt = Ventiladores.objects.all()
    busqueda_3 = request.GET.get("buscar")
    if busqueda_3:
        resultados_vt = Ventiladores.objects.filter(
            Q(nombre__icontains=busqueda_3) | 
            Q(descripcion__icontains=busqueda_3)
        ).distinct()
    return render(request, 'search_ventilador.html', {'resultados_vt': resultados_vt})

def ver_repuestos(request, nombre_ventilador):
    repuestos = Task.objects.filter(modelo_vt__icontains=nombre_ventilador)
    return render(request, 'task/task.html', {
        'tasks': repuestos,
        'nombre_ventilador': nombre_ventilador
        })


def ver_despiece(request, nombre_ventilador):
    despiece = Ventiladores.objects.filter(nombre__iexact=nombre_ventilador)
    return render(request, 'search_ventilador.html', {
        'resultados_vt': despiece, 
        'query': nombre_ventilador
        })

def create_task(request):   
    if request.method == 'POST':
        form = CreateNewTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/task/')
    else:
        form = CreateNewTaskForm()

    return render(request, 'task/create_task.html', {'form': form})
        
def create_project(request):
    if request.method == 'POST':
        form = CreateNewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/projects/')
    else:
        form = CreateNewProjectForm()

    return render(request, 'projects/create_project.html', {'form': form})

def repuestos_editar(request, id):
    repuesto = Task.objects.get(id=id)

    if request.method == "POST":
        form = CreateNewTaskForm(request.POST, request.FILES, instance=repuesto)
        if form.is_valid():
            form.save()
            return redirect("/task/")

    else:
        form = CreateNewTaskForm(instance=repuesto)

    context = {
        "form": form,
        "repuesto": repuesto,
    }

    return render(request, "task/edit.html", context)

def editar_ventilador(request, id):
    ventilador = Project.objects.get(id=id)
    
    if request.method == "POST":
        form = CreateNewProjectForm(request.POST, request.FILES, instance=ventilador)
        if form.is_valid():
            form.save()
            return redirect('/projects/')
        
    else:
        form = CreateNewProjectForm(instance=ventilador)
        
    context = {
        "form" : form,
        "ventilador" : ventilador
    } 
    
    return render(request,"projects/editVentilador.html", context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'El repuesto se eliminó correctamente.')

    return redirect('/task/')

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, 'El ventilador se eliminó correctamente')
    
    return redirect ('/projects/')