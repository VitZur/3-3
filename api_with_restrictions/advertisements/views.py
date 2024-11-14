from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter

class AdvertisementViewSet(viewsets.ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_class = AdvertisementFilter
    throttle_classes =  [AnonRateThrottle,UserRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_destroy(self, instance):
        if instance.creator != self.request.user:
            raise PermissionDenied("You do not have permission to delete this advertisement.")
        instance.delete()

    def perform_update(self,serializer):
        if serializer.instance.creator != self.request.user:
            raise PermissionDenied("You do not have permission to up")