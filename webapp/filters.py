import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class SermonFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    # end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    # note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = Sermons
        fields = '__all__'
        exclude = ['date_added']