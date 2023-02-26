import django_filters
from .models import Counslat

class FliterCounslat(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Counslat
        fields = ['name','catgoray']
