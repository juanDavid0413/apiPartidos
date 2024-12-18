from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartidosViewSet

router = DefaultRouter()
router.register(r'partidos', PartidosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]

