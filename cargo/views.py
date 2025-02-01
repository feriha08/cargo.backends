from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cargo
from .serializers import CargoSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    # Custom action to mark cargo as received
    @action(detail=True, methods=['post'])
    def receive(self, request, pk=None):
        cargo = self.get_object()
        cargo.is_received = True
        cargo.received_by = request.data.get('receivedBy')
        cargo.identification_number = request.data.get('identificationNumber')
        cargo.received_at = timezone.now()
        cargo.save()
        return Response({"status": "Cargo received"})
