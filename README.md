# django_commercial_property
Step 1: Project Setup
Create a Virtual Environment:-
in bash :
python -m venv myenv


Activate the Virtual Environment:

On macOS/Linux: (bash)
source myenv/bin/activate

On Windows(bash) :
.\myenv\Scripts\activate

Install Django:

pip install django

Create Django Project:

django-admin startproject commercial_project

Navigate to the Project Directory:
cd commercial_project


Step 2: App Creation
Create a Django App:
python manage.py startapp commercial_app


Step 3: Model, Views, Templates, and Forms
Models (models.py):

# commercial_app/models.py
from django.db import models

class CommercialProperty(models.Model):
    # ... Your model fields ...

Views (views.py):
# commercial_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from .models import CommercialProperty
from .forms import CommercialPropertyForm

# ... Your views classes ...


Forms (forms.py):
# commercial_app/forms.py
from django import forms
from .models import CommercialProperty

class CommercialPropertyForm(forms.ModelForm):
    class Meta:
        model = CommercialProperty
        fields = '__all__'

Step 4: URL Configuration
urls.py in commercial_app:

# commercial_app/urls.py
from django.urls import path
from .views import (
    PropertyListView,
    PropertyDetailView,
    PropertyCreateView,
    PropertyUpdateView,
    PropertyDeleteView,
)

urlpatterns = [
    path('properties/', PropertyListView.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('properties/create/', PropertyCreateView.as_view(), name='property-create'),
    path('properties/<int:pk>/update/', PropertyUpdateView.as_view(), name='property-update'),
    path('properties/<int:pk>/delete/', PropertyDeleteView.as_view(), name='property-delete'),
]


Project-level urls.py:
# commercial_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('commercial_app.urls')),
]



Step 5: Database Migration
python manage.py makemigrations
python manage.py migrate

Step 6: Create Superuser
python manage.py createsuperuser

Step 7: Static and Media Configuration (if needed)
# commercial_project/settings.py
# Add the following for static and media configuration

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

Step 8: Templates
Create HTML templates in the commercial_app/templates/commercial_app/ directory, such as property_list.html, property_detail.html, property_form.html, and property_confirm_delete.html.

Step 9: JSON Data (Sample)
Create a JSON file with sample data:

[
  {
    "address01": "Sample Address 1",
    "building_type": "Sample Type",
    "ownership": "Sample Ownership",
    "lot_size": 100,
    "building_size": 200,
    "price_per_square_meter": 10.5,
    "total_asking_price": 2100.0,
    "total_price_offered": 2000.0,
    "total_price_agreed": 2000.0,
    "deal_status": "FOR SALE",
    "listing_date": "2023-01-01",
    "listing_agent_name": "Agent 1",
    "listing_agent_phone": "1234567890",
    "description": "Sample description",
    "deal_comments": "Sample comments"
  },
  // Add more entries as needed
]


Step 10: Pytest Tests
Create test files in commercial_app/tests/:

test_views.py:
# commercial_app/tests/test_views.py
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest
from .models import CommercialProperty

@pytest.mark.django_db
def test_property_create_view(client):
    # ... Your test code ...

@pytest.mark.django_db
def test_property_detail_view(client):
    # ... Your test code ...

@pytest.mark.django_db
def test_property_update_view(client):
    # ... Your test code ...

@pytest.mark.django_db
def test_property_delete_view(client):
    # ... Your test code ...

test_forms.py:
# commercial_app/tests/test_forms.py
import pytest
from .forms import CommercialPropertyForm

@pytest.mark.django_db
def test_commercial_property_form_valid():
    # ... Your test code ...

@pytest.mark.django_db
def test_commercial_property_form_invalid():
    # ... Your test code ...



test_models.py:
# commercial_app/tests/test_models.py
import pytest
from .models import CommercialProperty

@pytest.mark.django_db
def test_commercial_property_model():
    # ... Your test code ...

Step 11: Run Pytest

pytest commercial_app/tests


Step 12: Run Development Server

python manage.py runserver

Now you should be able to access the Django admin site, manage your CommercialProperty objects, and test the CRUD operations using the provided views and forms.

This guide covers the essential steps and code for setting up a Django project with CRUD functionality, testing with Pytest, and handling static files and media.












