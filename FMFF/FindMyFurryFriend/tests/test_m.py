from django.test import TestCase
from .models import LostPet

class LostPetTestCase(TestCase):
    def setUp(self):
        # Create test data
        LostPet.objects.create(name="Test Pet", species="Dog", description="This is a test pet")

    def test_lost_pet_name(self):
        # Get the test pet
        test_pet = LostPet.objects.get(name="Test Pet")

        # Check if the pet's name matches what we created in setUp
        self.assertEqual(test_pet.name, "Test Pet")
