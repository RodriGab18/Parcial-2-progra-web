from rest_framework import serializers
from .models import Tarea


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'curso', 'fechaEntrega', 'estado']
        read_only_fields = ['id', 'estado']