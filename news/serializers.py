from rest_framework import serializers
from .models import ThreeNews

class ThreeNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeNews
        fields = '__all__'