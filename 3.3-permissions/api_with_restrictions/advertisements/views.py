from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied


from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advetsement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [permutations.IsAuthenticated()]
        return [permutations.AllowAny()]

    def perform_create(self, serializer):
        if self.request.user.advertisements.filter(status=Advertisement.OPEN) >=10:
            raise serializer.ValidationError("You can't have more than 10 open advertisements.")
        serializer.save(author=self.author.user)

    def destroy(self,request,*args,**kwargs):
        advertisement = self.get_object()
        if advertisement.author != request.user:
            raise PermissionDenied("You can only  delete your own advertisements")
        return super().destoy(request,*args,**kwargs)