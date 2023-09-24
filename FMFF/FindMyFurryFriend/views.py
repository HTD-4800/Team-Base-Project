# FindMyFurryFriend/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import LostPet 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .filters import LostPetFilter
from django.contrib.auth.models import User
from django.http import HttpResponse


def lost_pet_list(request):
    # Create a filter instance and apply it to the queryset
    lost_pet_filter = LostPetFilter(request.GET, queryset=LostPet.objects.all())

    # Check if the form has been submitted and if it is valid
    if request.method == 'GET' and lost_pet_filter.is_valid():
        # Apply the filter to the queryset
        lost_pets = lost_pet_filter.qs
    else:
        # If the form is not submitted or is not valid, display all lost pets
        lost_pets = LostPet.objects.all()

    return render(request, 'FindMyFurryFriend/lost_pet_list.html', {'lost_pets': lost_pets, 'filter': lost_pet_filter})

def add_lost_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        description = request.POST.get('description')

        if request.user.is_authenticated:
            owner = request.user
        else:
            owner = None  # No authenticated user (guest user)

        if name and species and description:
            new_lost_pet = LostPet(name=name, species=species, description=description, owner=owner)
            new_lost_pet.save()
            return redirect('lost_pet_list')
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

