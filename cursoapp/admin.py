from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Curso_Profesor)
admin.site.register(Tarea)