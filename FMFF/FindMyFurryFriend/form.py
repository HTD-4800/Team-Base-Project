from django import forms
from .models import LostPet

class LostPetForm(forms.ModelForm):
    class Meta:
        model = LostPet
        fields = ['name', 'species', 'description', 'image']
