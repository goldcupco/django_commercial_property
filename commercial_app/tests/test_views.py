# commercial_app/tests/test_views.py

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest
from commercial_app.models import CommercialProperty  # Add this import

@pytest.mark.django_db
def test_property_create_view(client):
    url = reverse('property-create')  # instead of 'property_create'

    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'commercial_app/property_form.html')

    # Add more assertions for form submission

@pytest.mark.django_db
def test_property_detail_view(client):
    property_instance = CommercialProperty.objects.create(address01='Test Address', building_type='Test Type', listing_date='2023-01-01')
    url = reverse('property-detail', args=[property_instance.pk])
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'commercial_app/property_detail.html')

    # Add assertions for displayed data, e.g., check if property details are present in the response content

@pytest.mark.django_db
def test_property_update_view(client):
    property_instance = CommercialProperty.objects.create(address01='Test Address', building_type='Test Type', listing_date='2023-01-01')
    url = reverse('property-update', args=[property_instance.pk])
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'commercial_app/property_form.html')

    # Add more assertions for form submission

@pytest.mark.django_db
def test_property_delete_view(client):
    property_instance = CommercialProperty.objects.create(address01='Test Address', building_type='Test Type', listing_date='2023-01-01')
    url = reverse('property-delete', args=[property_instance.pk])
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'commercial_app/property_confirm_delete.html')

    # Add more assertions for deletion confirmation
