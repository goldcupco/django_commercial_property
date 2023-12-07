# commercial_app/serializers.py
from rest_framework import serializers
from .models import CommercialProperty

class CommercialPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommercialProperty
        fields = '__all__'