from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=200)
    apellido_profesor = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_profesor + " " + self.apellido_profesor


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    creditos = models.IntegerField()
    descrip_curso = models.TextField()
    
    def __str__(self):
        return self.nombre_curso
    

class Curso_Profesor(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    horario = models.CharField(max_length=5)
    
    def __str__(self):
        return self.curso.nombre_curso + " - " + self.profesor.nombre_profesor

    
class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=200)
    descrip_tarea = models.TextField()
    curso_profesor = models.ForeignKey(Curso_Profesor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_tarea