from django_filters import rest_framework as filters

from advertisements.models import AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    date_range = filters.DateFromToRangeFilter(field_name='created_at')
    status = filters.ChoiceFilter(choise=AdvertisementStatusChoices.STATUS_CHOICES)

    class Meta:
        model = Advertisement
        fields = ['data_range','status']
    # TODO: задайте тре