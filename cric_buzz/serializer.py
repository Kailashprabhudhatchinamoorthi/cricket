from rest_framework import serializers
from .models import cric_profile

class cric_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = cric_profile
        fields = '__all__'
