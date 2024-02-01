from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.projects),
    path('search_ventilador/',views.ventilador_search),
    path('projects/', views.projects),
    path('create_project/', views.create_project),
    path('task/', views.task),
    path('create_task/', views.create_task),
    path('ver_repuestos/<str:nombre_ventilador>/', views.ver_repuestos, name='ver_repuestos'),
    path('ver_despiece/<str:nombre_ventilador>/', views.ver_despiece, name='ver_despiece'),
    path('repuestos/editar/<int:id>', views.repuestos_editar, name='repuestos_editar'),
    path('repuestos/eliminar/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('editar_ventilador/<int:id>/', views.editar_ventilador, name='editar_ventilador'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)