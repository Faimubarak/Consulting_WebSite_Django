import django_filters
from .models import Post

class FliterCounslat(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Post
        fields = ['title','catgoray',]
