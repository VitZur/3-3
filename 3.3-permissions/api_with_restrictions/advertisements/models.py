from django.conf import settings
from django.db import models
from django_filters import rest_framework as filters


class AdvertisementStatusChoices(models.TextChoices):

    OPEN = "OPEN", "Open"
    CLOSED = "CLOSED", "Close"
    DRAFT = "DRAFT", "Draft"


class Advertisement(models.Model):


    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Исправляем на `DateTimeField`

    def __str__(self):
        return self.title


class AdvertisementFilter(filters.FilterSet):
    date_range = filters.DateFromToRangeFilter(field_name='created_at')
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)  # Исправляем `choise` на `choices`

    class Meta:
        model = Advertisement
        fields = ['date_range', 'status']
