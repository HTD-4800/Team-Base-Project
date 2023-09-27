# filters.py
import django_filters
from .models import LostPet

class LostPetFilter(django_filters.FilterSet):
    class Meta:
        model = LostPet
        fields = ['species']  # Add the fields that are part of the LostPet model