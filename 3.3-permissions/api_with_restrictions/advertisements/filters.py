from django_filters import rest_framework as filters

from .models import AdvertisementStatusChoices,Advertisement


class AdvertisementFilter(filters.FilterSet):
    date_range = filters.DateFromToRangeFilter(field_name='created_at')
    status = filters.ChoiceFilter(choises=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['date_range','status']
    # TODO: задайте тре