from rest_framework import viewsets, permissions, views
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response

from .serializers import ApplicationSerializer
from .models import Application


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['post'])
    def generate_new_key(self, request, pk=None):
        obj = self.get_object()
        obj.generate_new_key()
        return Response({'status': 'new key has been generated'})


class TestView(views.APIView):
    def get(self, request, format=None):
        key = self.request.META.get('HTTP_X_API_KEY')
        application = Application.objects.filter(key=key).first()
        if not application:
            raise NotAuthenticated(detail='Please specify correct X-API-KEY header')
        return Response(ApplicationSerializer(application).data)

