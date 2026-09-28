from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.listar_tareas, name='listar_tareas'),
    path('tareas/<int:pk>/', views.detalle_tarea, name='detalle_tarea'),
    path('tareas/<int:pk>/completar/', views.completar_tarea, name='completar_tarea'),
]