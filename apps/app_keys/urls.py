from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ApplicationViewSet, TestView

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet, basename='application')
urlpatterns = [
    path('test', TestView.as_view(), name='application-test'),
]
urlpatterns += router.urls
