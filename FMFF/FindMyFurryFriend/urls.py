# FindMyFurryFriend/views.py
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'FindMyFurryFriend'

urlpatterns = [
    path('lost-pets/', views.lost_pet_list, name='lost_pet_list'),
    path('add-lost-pet/', views.add_lost_pet, name='add_lost_pet'),
    path('lost-pet/<int:pet_id>/', views.lost_pet_detail, name='lost_pet_detail'),
    path('TN-api/', views.TN_api, name='TN_api'),
    path('emergency-contacts/list/', TemplateView.as_view(template_name='FindMyFurryFriend/list.html'), name='emergency_contacts_list'),
]


