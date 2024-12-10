from rest_framework import serializers
from .models import Partidos

class PartidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partidos
        fields = '__all__'
