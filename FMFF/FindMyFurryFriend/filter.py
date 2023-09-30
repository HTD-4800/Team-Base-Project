import django_filters
from .models import LostPet

class LostPetFilter(django_filters.FilterSet):

    # Define additional filter fields
     #name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match
    # location = django_filters.CharFilter(lookup_expr='iexact')  # Case-insensitive exact match

    class Meta:
        model = LostPet
        fields = ['species', 'name']  # Add more fields as needed
