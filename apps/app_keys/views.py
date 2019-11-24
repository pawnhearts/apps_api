from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ApplicationSerializer
from .models import Application


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    @action(detail=True, methods=['post'])
    def generate_new_key(self, request, pk=None):
        obj = self.get_object()
        obj.generate_new_key()
        return Response({'status': 'new key has been generated'})

