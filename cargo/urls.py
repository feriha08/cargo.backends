from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CargoViewSet

router = DefaultRouter()
router.register(r'cargo', CargoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
