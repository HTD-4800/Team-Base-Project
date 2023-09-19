# accounts/urls.py

from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'accounts'  # Define an app_name for the 'accounts' app

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
]
