from django.contrib import admin
from .models import Task, Ventiladores, Project
# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Ventiladores)


