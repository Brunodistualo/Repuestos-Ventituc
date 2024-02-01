from django import forms
from .models import Task, Project

class CreateNewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'imagenes', 'modelo_vt']
    
class CreateNewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'imagenes']