from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Advertisement,AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):

        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("User must be authenticated to create an advertisement.")
        validated_data["creator"] = request.user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context["request"].user
        open_ads_count = Advertisement.objects.filter(
            creator=user,
            status=AdvertisementStatusChoices.OPEN
        ).count()

        if data.get('status') == AdvertisementStatusChoices.OPEN and open_ads_count >= 10:
            raise serializers.ValidationError(
                "You can't have more than 10 open advertisements."
            )
        return data