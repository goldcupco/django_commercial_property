# commercial_app/forms.py

from django import forms
from .models import CommercialProperty

class CommercialPropertyForm(forms.ModelForm):
    class Meta:
        model = CommercialProperty
        fields = '__all__'
