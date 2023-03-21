from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from .models import *

#Cursos
def cursos(request):
    cursos = Curso.objects.all()
    return render(request,'Curso/cursos.html',{
        'cursos' : cursos
    })


def agregar_curso(request):
    if request.method == 'GET':
        return render(request,'layouts/form.html',{
            'form' : Curso_Form(),
            'url' : 'mostrar_cursos',
            'accion' : 'Agregando un Curso'
        })
    else:
        Curso.objects.create(nombre_curso = request.POST['nombre_curso'],
                             creditos = int(request.POST['creditos']),
                             descrip_curso = request.POST['descrip_curso'])
        return redirect('mostrar_cursos')
    
    
def editar_curso(request, id):
    curso = get_object_or_404(Curso, id = id)
    if request.method == 'GET':
        return render(request,'layouts/form.html',{
            'form' : Curso_Form(instance=curso),
            'accion' : 'Editando el Curso ' + str(id),
            'url' : 'mostrar_cursos'
        })
    else:
        Curso.objects.filter(id = id).update(nombre_curso = request.POST['nombre_curso'],
                                             creditos = int(request.POST['creditos']),
                                             descrip_curso = request.POST['descrip_curso'])
        return redirect('mostrar_cursos')
    
    
def borrar_curso(request, id):
    if request.method == 'POST':
        Curso.objects.filter(id = id).delete()
        return redirect('mostrar_cursos')
    
    
    
#Profesores
def profesores(request):
    profesores = Profesor.objects.all()
    return render(request,'Profesor/profesores.html',{
        'profesores' : profesores
    })


def agregar_profesor(request):
    if request.method == 'GET':
        return render(request,'layouts/form.html',{
            'form' : Profesor_Form(),
            'url' : 'mostrar_profesores',
            'accion' : 'Agregando un Profesor'
        })
    else:
        Profesor.objects.create(nombre_profesor=request.POST['nombre_profesor'],
                                apellido_profesor=request.POST['apellido_profesor'])
        return redirect('mostrar_profesores')
    
    
def editar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id = id)
    if request.method == 'GET':
        return render(request,'layouts/form.html',{
            'form' : Profesor_Form(instance=profesor),
            'accion' : 'Editando el Profesor ' + str(id),
            'url' : 'mostrar_profesores'
        })
    else:
        Profesor.objects.filter(id = id).update(nombre_profesor=request.POST['nombre_profesor'],
                                                apellido_profesor=request.POST['apellido_profesor'])
        return redirect('mostrar_profesores')
    
    
def borrar_profesor(request, id):
    if request.method == 'POST':
        Profesor.objects.filter(id = id).delete()
        return redirect('mostrar_profesores')
    
    
    
#Horarios
def horarios(request):
    horarios = Curso_Profesor.objects.all().select_related('curso','profesor')
    return render(request,'Horario/horarios.html',{
        'horarios' : horarios
    })


def agregar_horario(request):
    if request.method == 'GET':
        return render(request,'layouts/form.html',{
            'form' : Horario_Form(),
            'url' : 'mostrar_horarios',
            'accion' : 'Agregando un Horario'
        })
    else:
        Curso_Profesor.objects.create(curso_id = request.POST['curso'],
                                      profesor_id = request.POST['profesor'],
                                      horario = request.POST['horario'])
        return redirect('mostrar_horarios')
    
    
def editar_horario(request, id):
    horario = get_object_or_404(Curso_Profesor, id = id)
    if request.method == 'GET':
        return render(request,'layouts/form.html',{
            'form' : Horario_Form(instance=horario),
            'accion' : 'Editando el Horario ' + str(id),
            'url' : 'mostrar_horarios'
        })
    else:
        Curso_Profesor.objects.filter(id = id).update(curso_id = request.POST['curso'],
                                                      profesor_id = request.POST['profesor'],
                                                      horario = request.POST['horario'])
        return redirect('mostrar_horarios')
    
    
def borrar_horario(request, id):
    if request.method == 'POST':
        Curso_Profesor.objects.filter(id = id).delete()
        return redirect('mostrar_horarios')
    
    
#Tareas
def tareas(request):
    tareas =Tarea.objects.all().select_related('curso_profesor')
    return render(request,'Tarea/tareas.html',{
        'tareas' : tareas
    })


def agregar_tarea(request):
    if request.method == 'GET':
        return render(request,'layouts/form.html',{
            'form' : Tarea_Form(),
            'url' : 'mostrar_tareas',
            'accion' : 'Agregando una Tarea'
        })
    else:
        Tarea.objects.create(nombre_tarea = request.POST['nombre_tarea'],
                             descrip_tarea = request.POST['descrip_tarea'],
                             curso_profesor_id = request.POST['curso_profesor'])
        return redirect('mostrar_tareas')
    
    
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id = id)
    if request.method == 'GET':
        return render(request,'layouts/form.html',{
            'form' : Tarea_Form(instance=tarea),
            'accion' : 'Editando la Tarea ' + str(id),
            'url' : 'mostrar_tareas'
        })
    else:
        Tarea.objects.filter(id = id).update(nombre_tarea = request.POST['nombre_tarea'],
                                             descrip_tarea = request.POST['descrip_tarea'],
                                             curso_profesor_id = request.POST['curso_profesor'])
        return redirect('mostrar_tareas')
    
    
def borrar_tarea(request, id):
    if request.method == 'POST':
        Tarea.objects.filter(id = id).delete()
        return redirect('mostrar_tareas')