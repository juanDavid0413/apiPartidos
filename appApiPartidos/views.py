from django.shortcuts import render
from rest_framework import viewsets
from .models import Partidos
from .serializers import PartidosSerializer

class PartidosViewSet(viewsets.ModelViewSet):
    queryset = Partidos.objects.all()
    serializer_class = PartidosSerializer