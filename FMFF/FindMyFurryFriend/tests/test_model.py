# test_model.py

from django.test import TestCase
from django.contrib.auth.models import User
from ..models import LostPet

class LostPetModelTest(TestCase):

    def test_lost_pet_str_representation(self):
        # Create a User instance
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a LostPet instance
        lost_pet = LostPet.objects.create(owner=user, name='Fluffy', species='Dog', description='A cute dog')

        # Check if the __str__ method returns the expected string representation
        self.assertEqual(str(lost_pet), 'Fluffy')

