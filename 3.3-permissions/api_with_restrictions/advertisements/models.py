from django.conf import settings
from django.db import models
from django_filters import rest_framework as filters

class AdvertisementStatusChoices(models.TextChoices):
    ACTIVE = 'active', 'Active'
    INACTIVE = 'inactive', 'Inactive'
    PENDING = 'pending', 'Pending'
    OPEN = 'open', 'Open'
    CLOSE = 'close', 'Close'

class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AdvertisementFilter(filters.FilterSet):
    date_range = filters.DateFromToRangeFilter(
        field_name='created_at',
        label='Created at range'
    )
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['date_range', 'status']
