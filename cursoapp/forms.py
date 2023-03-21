from django import forms
from .models import Curso, Profesor, Curso_Profesor
from .models import *

class Profesor_Form(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombre_profesor','apellido_profesor')
        labels = {
            'nombre_profesor' : 'Nombre(s) del Profesor',
            'apellido_profesor' : 'Apellido(s) del Profesor'
        }
        widgets = {
            'nombre_profesor' : forms.TextInput(attrs={'class' : 'form-control'}),
            'apellido_profesor' : forms.TextInput(attrs={'class' : 'form-control'})
        }
    
    
class Curso_Form(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre_curso','creditos','descrip_curso')
        labels = {
            'nombre_curso' : 'Nombre del Curso',
            'creditos' : 'Cantidad de creditos',
            'descrip_curso' : 'Descripcion del Curso'
        }
        widgets = {
            'nombre_curso' : forms.TextInput(attrs={'class' : 'form-control'}),
            'creditos' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'descrip_curso' : forms.Textarea(attrs={'class' : 'form-control'})
        }

    
class Horario_Form(forms.ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), 
                                   empty_label='(---Curso---)',
                                   widget=forms.Select(attrs={'class' : 'form-select'}))
    profesor = forms.ModelChoiceField(queryset=Profesor.objects.all(), 
                                      empty_label='(---Profesor---)', 
                                      widget=forms.Select(attrs={'class' : 'form-select'}))
    class Meta:
        model = Curso_Profesor
        fields = ('curso','profesor','horario')
        labels = {
            'curso' : 'Seleccione un curso',
            'profesor' : 'Seleccione un profesor',
            'horario' : 'Ingrese el horario'
        }
        widgets = {
            'horario' : forms.TextInput(attrs={'class' : 'form-control'})
        }
    

class Tarea_Form(forms.ModelForm):
    nombre_tarea = forms.CharField(label='Nombre de la Tarea ', 
                                   max_length=200,
                                   widget=forms.TextInput(attrs={'class' : 'form-control'}))
    descrip_tarea = forms.CharField(label='Descripcion de la Tarea ', 
                                    widget=forms.Textarea(attrs={'class' : 'form-control'}))
    curso_profesor = forms.ModelChoiceField(label='Seleccione el curso y el profesor que asigno la tarea ', 
                                            queryset=Curso_Profesor.objects.all(), 
                                            empty_label='(---Curso/Profesor---)', 
                                            widget=forms.Select(attrs={'class' : 'form-select'}))
    class Meta:
        model = Tarea
        fields = ('nombre_tarea','descrip_tarea','curso_profesor')