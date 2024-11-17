from rest_framework import viewsets, permissions
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
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Права доступа на основе действия."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_destroy(self, instance):
        """Удаление объявления с проверкой прав."""
        if instance.creator != self.request.user:
            raise PermissionDenied("You do not have permission to delete this advertisement.")
        instance.delete()

    def perform_update(self, serializer):
        """Обновление объявления с проверкой прав."""
        if serializer.instance.creator != self.request.user:
            raise PermissionDenied("You do not have permission to update this advertisement.")
        serializer.save()
