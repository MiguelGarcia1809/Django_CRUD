from django.urls import path
from cursoapp import views

urlpatterns = [
    
    #Al iniciar el servidor
    path('',views.cursos, name='index'),
    
    #Cursos
    path('mostrar_cursos/',views.cursos, name='mostrar_cursos'),
    path('agregar_curso/',views.agregar_curso, name='agregar_curso'),
    path('editar_curso/<int:id>/',views.editar_curso, name='editar_curso'),
    path('borrar_curso/<int:id>/',views.borrar_curso, name='borrar_curso'),
    
    #Profesores
    path('mostrar_profesores/',views.profesores, name='mostrar_profesores'),
    path('agregar_profesor/',views.agregar_profesor, name='agregar_profesor'),
    path('editar_profesor/<int:id>/',views.editar_profesor, name='editar_profesor'),
    path('borrar_profesor/<int:id>/',views.borrar_profesor, name='borrar_profesor'),
    
    #Horarios
    path('mostrar_horarios/',views.horarios, name='mostrar_horarios'),
    path('agregar_horario/',views.agregar_horario, name='agregar_horario'),
    path('editar_horario/<int:id>/',views.editar_horario, name='editar_horario'),
    path('borrar_horario/<int:id>/',views.borrar_horario, name='borrar_horario'),
    
    #Tareas
    path('mostrar_tareas/',views.tareas, name='mostrar_tareas'),
    path('agregar_tarea/',views.agregar_tarea, name='agregar_tarea'),
    path('editar_tarea/<int:id>/',views.editar_tarea, name='editar_tarea'),
    path('borrar_tarea/<int:id>/',views.borrar_tarea, name='borrar_tarea'),
]