from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Tarea
from .serializers import TareaSerializer


@api_view(['GET'])
def listar_tareas(request):
    """
    GET /api/tareas/
    GET /api/tareas/?estado=pendiente
    GET /api/tareas/?estado=completada
    """
    estado = request.query_params.get('estado')
    tareas = Tarea.objects.all()

    if estado:
        if estado not in ['pendiente', 'completada']:
            return Response(
                {'error': 'Estado inválido. Use "pendiente" o "completada".'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        tareas = tareas.filter(estado=estado)

    serializer = TareaSerializer(tareas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detalle_tarea(request, pk):
    """
    GET /api/tareas/<id>/
    """
    tarea = get_object_or_404(Tarea, pk=pk)
    serializer = TareaSerializer(tarea)
    return Response(serializer.data)


@api_view(['PATCH'])
def completar_tarea(request, pk):
    """
    PATCH /api/tareas/<id>/completar/
    """
    tarea = get_object_or_404(Tarea, pk=pk)

    if tarea.estado == 'completada':
        return Response(
            {'mensaje': 'La tarea ya estaba completada.'},
            status=status.HTTP_200_OK,
        )

    tarea.estado = 'completada'
    tarea.save()

    serializer = TareaSerializer(tarea)
    return Response(serializer.data, status=status.HTTP_200_OK)