# FindMyFurryFriend/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import LostPet 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def lost_pet_list(request):
    lost_pets = LostPet.objects.all()
    return render(request, 'FindMyFurryFriend/lost_pet_list.html', {'lost_pets': lost_pets})

@login_required
def add_lost_pet(request):
    if request.method == 'POST':
        # Handle the form submission to add a new lost pet listing
        name = request.POST.get('name')
        species = request.POST.get('species')
        description = request.POST.get('description')

        # Get the currently logged-in user
        owner = request.user  # This should now be a valid User instance

        # Check if all required fields are provided
        if name and species and description:
            # Create a new LostPet object with the owner information
            new_lost_pet = LostPet(name=name, species=species, description=description, owner=owner)
            new_lost_pet.save()  # Save the new pet listing to the database

            return redirect('lost_pet_list')  # Redirect to the list of lost pets after adding one
        else:
            # Handle form validation errors here (e.g., display an error message)
            pass

    return render(request, 'FindMyFurryFriend/add_lost_pet.html')

def lost_pet_detail(request, pet_id):
    # Retrieve the specific LostPet object with the given pet_id, or return a 404 error if not found
    pet = get_object_or_404(LostPet, pk=pet_id)
    return render(request, 'FindMyFurryFriend/lost_pet_detail.html', {'pet': pet})


def TN_api(request):
    print("TN_api view called")
    data = {'message': 'Hello, this is Thoa first HTTP API!'}
    return JsonResponse(data)
 